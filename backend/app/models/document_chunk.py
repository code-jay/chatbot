from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime, UTC
from app.db.base import Base


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    conversation_id = Column(Integer, ForeignKey("conversations.id"), nullable=False)
    file_id = Column(Integer, ForeignKey("uploaded_files.id"), nullable=False)
    content = Column(Text)
    embedding = Column(Text)
    created_at = Column(DateTime, default=datetime.now(UTC))