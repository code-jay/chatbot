from sqlalchemy.orm import Session

from app.models import UsageLog, User


def save_usage_log(
    db: Session,
    current_user: User,
    conversation_id: int,
    model: str,
    user_message: str,
    assistant_reply: str
):
    usage_log = UsageLog(
        user_id=current_user.id,
        conversation_id=conversation_id,
        model=model,
        prompt_tokens=len(user_message.split()),
        completion_tokens=len(assistant_reply.split()),
        total_tokens=len(user_message.split()) + len(assistant_reply.split())
    )

    db.add(usage_log)
    db.commit()

    return usage_log