from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime, UTC
from app.db.base import Base

class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(
    Integer,
    ForeignKey("users.id"),
    nullable=False
    )
    conversation_id = Column(
    Integer,
    ForeignKey("conversations.id"),
    nullable=False)
    filename = Column(String)
    file_path = Column(String)
    content_type = Column(String)
    created_at = Column(DateTime, default=datetime.now(UTC))