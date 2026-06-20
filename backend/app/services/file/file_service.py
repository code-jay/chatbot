import json
from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models import User, UploadedFile, DocumentChunk
from app.services.chat.conversation_service import get_or_create_conversation
from app.services.file.storage_service import save_uploaded_file
from app.services.file.extraction_service import extract_text_from_file
from app.services.rag.chunking_service import chunk_text
from app.services.rag.embedding_service import create_embedding


def upload_document(
    conversation_id: int | None,
    file: UploadFile,
    db: Session,
    current_user: User
):
    if file.content_type not in settings.ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, TXT, and Markdown files are supported."
        )

    conversation = get_or_create_conversation(
        db=db,
        current_user=current_user,
        conversation_id=conversation_id,
        title=file.filename[:40] if file.filename else "Uploaded Document"
    )

    try:
        uploaded_file = UploadedFile(
            user_id=current_user.id,
            conversation_id=conversation.id,
            filename=file.filename,
            content_type=file.content_type,
            file_path=""
        )

        db.add(uploaded_file)
        db.flush()

        saved_file_path = save_uploaded_file(
            file=file,
            file_id=uploaded_file.id
        )

        uploaded_file.file_path = str(saved_file_path)

        text = extract_text_from_file(
            file_path=str(saved_file_path),
            content_type=file.content_type
        )

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the uploaded file."
            )

        chunks = chunk_text(text)

        for chunk in chunks:
            embedding = create_embedding(chunk)

            doc_chunk = DocumentChunk(
                user_id=current_user.id,
                conversation_id=conversation.id,
                file_id=uploaded_file.id,
                content=chunk,
                embedding=json.dumps(embedding)
            )

            db.add(doc_chunk)

        db.commit()
        db.refresh(uploaded_file)

        return {
            "id": uploaded_file.id,
            "filename": uploaded_file.filename,
            "content_type": uploaded_file.content_type,
            "chunks": len(chunks),
            "conversation_id": conversation.id,
        }

    except HTTPException:
        db.rollback()
        raise

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )