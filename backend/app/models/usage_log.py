from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime, UTC
from app.db.base import Base

class UsageLog(Base):
    __tablename__ = "usage_logs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(
    Integer,
    ForeignKey("users.id"),
    nullable=False)
    conversation_id = Column(
    Integer,
    ForeignKey("conversations.id"),
    nullable=False)
    model = Column(String)
    prompt_tokens = Column(Integer, default=0)
    completion_tokens = Column(Integer, default=0)
    total_tokens = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now(UTC))