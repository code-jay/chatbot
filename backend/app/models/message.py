from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime, UTC
from app.db.base import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(
    Integer,
    ForeignKey("conversations.id"),
    nullable=False)
    role = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now(UTC))
