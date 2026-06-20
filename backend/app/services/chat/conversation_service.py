from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Conversation, User, Message, DocumentChunk, UploadedFile, UsageLog



def get_or_create_conversation(
    db: Session,
    current_user: User,
    conversation_id: int | None,
    title: str
) -> Conversation:
    """
    Get existing conversation or create a new one.
    """

    if conversation_id:
        conversation = (
            db.query(Conversation)
            .filter(
                Conversation.id == conversation_id,
                Conversation.user_id == current_user.id
            )
            .first()
        )

        if not conversation:
            raise HTTPException(
                status_code=404,
                detail="Conversation not found."
            )

        return conversation

    conversation = Conversation(
        user_id=current_user.id,
        title=title[:40] if title else "New Conversation"
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation


def get_conversation(
    db: Session,
    conversation_id: int,
    current_user: User
) -> Conversation:
    """
    Fetch a conversation belonging to the current user.
    """

    conversation = (
        db.query(Conversation)
        .filter(
            Conversation.id == conversation_id,
            Conversation.user_id == current_user.id
        )
        .first()
    )

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found."
        )

    return conversation


def list_user_conversations(
    db: Session,
    current_user: User
):
    """
    Return all conversations for the current user.
    """

    return (
        db.query(Conversation)
        .filter(
            Conversation.user_id == current_user.id
        )
        .order_by(
            Conversation.created_at.desc()
        )
        .all()
    )

def delete_user_conversation(
    db: Session,
    current_user: User,
    conversation_id: int
):
    conversation = (
        db.query(Conversation)
        .filter(
            Conversation.id == conversation_id,
            Conversation.user_id == current_user.id
        )
        .first()
    )

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    db.query(DocumentChunk).filter(
        DocumentChunk.conversation_id == conversation_id,
        DocumentChunk.user_id == current_user.id
    ).delete(synchronize_session=False)

    db.query(UploadedFile).filter(
        UploadedFile.conversation_id == conversation_id,
        UploadedFile.user_id == current_user.id
    ).delete(synchronize_session=False)

    db.query(UsageLog).filter(
        UsageLog.conversation_id == conversation_id,
        UsageLog.user_id == current_user.id
    ).delete(synchronize_session=False)

    db.query(Message).filter(
        Message.conversation_id == conversation_id
    ).delete(synchronize_session=False)

    db.delete(conversation)
    db.commit()

    return {"status": "deleted"}