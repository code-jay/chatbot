import json

from sqlalchemy.orm import Session

from app.models import DocumentChunk
from app.services.rag.embedding_service import create_embedding
from app.services.rag.similarity_service import cosine_similarity


def retrieve_relevant_chunks(
    query: str,
    conversation_id: int,
    user_id: int,
    db: Session,
    top_k: int = 4
):
    query_embedding = create_embedding(query)

    chunks = db.query(DocumentChunk).filter(
        DocumentChunk.user_id == user_id,
        DocumentChunk.conversation_id == conversation_id
    ).all()

    scored_chunks = []

    for chunk in chunks:
        chunk_embedding = json.loads(chunk.embedding)

        score = cosine_similarity(
            query_embedding,
            chunk_embedding
        )

        scored_chunks.append({
            "content": chunk.content,
            "score": score
        })

    scored_chunks.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return scored_chunks[:top_k]