from sqlalchemy.orm import Session

from app.models import User
from app.services.chat.conversation_service import get_or_create_conversation
from app.services.chat.message_service import save_message, get_previous_messages
from app.services.chat.prompt_builder import build_chat_prompt
from app.services.chat.usage_service import save_usage_log


def prepare_chat_context(
    db: Session,
    current_user: User,
    message: str,
    conversation_id: int | None,
    retrieve_relevant_chunks
):
    conversation = get_or_create_conversation(
        db=db,
        current_user=current_user,
        conversation_id=conversation_id,
        title=message
    )

    save_message(
        db=db,
        conversation_id=conversation.id,
        role="user",
        content=message
    )

    relevant_chunks = retrieve_relevant_chunks(
        query=message,
        conversation_id=conversation.id,
        user_id=current_user.id,
        db=db
    )

    rag_context = "\n\n".join(
        [chunk["content"] for chunk in relevant_chunks]
    )

    previous_messages = get_previous_messages(
        db=db,
        conversation_id=conversation.id
    )

    input_messages = build_chat_prompt(
        previous_messages=previous_messages,
        rag_context=rag_context
    )

    return conversation, input_messages


def save_chat_response(
    db: Session,
    current_user: User,
    conversation_id: int,
    user_message: str,
    assistant_reply: str,
    model: str
):
    save_message(
        db=db,
        conversation_id=conversation_id,
        role="assistant",
        content=assistant_reply
    )

    save_usage_log(
        db=db,
        current_user=current_user,
        conversation_id=conversation_id,
        model=model,
        user_message=user_message,
        assistant_reply=assistant_reply
    )