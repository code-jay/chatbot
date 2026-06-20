from fastapi import APIRouter, Depends, Request
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.chat import ChatRequest
from app.models import User

from app.core.dependencies import get_current_user
from app.core.rate_limit import limiter

from app.core.providers import ai_gateway
from app.services.chat.chat_service import (
    prepare_chat_context,
    save_chat_response
)

from app.services.rag.retrieval_service import (
    retrieve_relevant_chunks
)

router = APIRouter()



@router.post("/chat/stream")
@limiter.limit("10/minute")
def chat_stream(
    request: Request,
    req: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    conversation, input_messages = prepare_chat_context(
        db=db,
        current_user=current_user,
        message=req.message,
        conversation_id=req.conversation_id,
        retrieve_relevant_chunks=retrieve_relevant_chunks
    )

    def generate():
        full_reply = ""
        selected_model = "gpt-4.1-mini"

        for delta, model in ai_gateway.stream_response(
            input_messages,
            req.message
        ):
            selected_model = model
            full_reply += delta
            yield delta

        save_chat_response(
            db=db,
            current_user=current_user,
            conversation_id=conversation.id,
            user_message=req.message,
            assistant_reply=full_reply,
            model=selected_model
        )

    return StreamingResponse(
        generate(),
        media_type="text/plain",
        headers={
            "X-Conversation-Id": str(conversation.id)
        }
    )