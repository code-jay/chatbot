from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime, UTC
from app.db.base import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column( Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, default="New Chat")
    created_at = Column(DateTime, default=datetime.now(UTC))