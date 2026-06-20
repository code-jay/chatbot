from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, UTC
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, default="user")
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC))