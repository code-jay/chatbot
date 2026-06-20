from sqlalchemy.orm import Session

from app.models import (
    User,
    Conversation,
    Message,
    UploadedFile,
    DocumentChunk,
    UsageLog
)


def get_admin_stats(db: Session):
    return {
        "users": db.query(User).count(),
        "conversations": db.query(Conversation).count(),
        "messages": db.query(Message).count(),
        "files": db.query(UploadedFile).count(),
        "chunks": db.query(DocumentChunk).count(),
        "usage_logs": db.query(UsageLog).count(),
    }


def get_all_users(db: Session):
    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "created_at": user.created_at,
        }
        for user in users
    ]


def get_usage_logs(
    db: Session,
    limit: int = 100
):
    logs = (
        db.query(UsageLog)
        .order_by(UsageLog.created_at.desc())
        .limit(limit)
        .all()
    )

    return [
        {
            "user_id": log.user_id,
            "conversation_id": log.conversation_id,
            "model": log.model,
            "prompt_tokens": log.prompt_tokens,
            "completion_tokens": log.completion_tokens,
            "total_tokens": log.total_tokens,
            "created_at": log.created_at,
        }
        for log in logs
    ]