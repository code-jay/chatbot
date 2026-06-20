from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import User
from app.core.dependencies import get_current_user

from app.services.chat.conversation_service import (
    list_user_conversations,
    delete_user_conversation,
    get_conversation,
)

from app.services.chat.message_service import (
    get_conversation_messages,
)


router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)


@router.get("")
def list_conversations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return list_user_conversations(
        db=db,
        current_user=current_user
    )


@router.delete("/{conversation_id}")
def delete_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return delete_user_conversation(
            db=db,
            current_user=current_user,
            conversation_id=conversation_id
        )

    except HTTPException:
        raise

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/{conversation_id}/messages")
def get_messages(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    get_conversation(
        db=db,
        conversation_id=conversation_id,
        current_user=current_user
    )

    return get_conversation_messages(
        db=db,
        conversation_id=conversation_id
    )