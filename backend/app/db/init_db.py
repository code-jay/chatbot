from app.db.base import Base
from app.db.database import engine

from app.models.user import User
from app.models.conversation import Conversation
from app.models.message import Message
from app.models.upload_file import UploadedFile
from app.models.document_chunk import DocumentChunk
from app.models.usage_log import UsageLog


def init_db():
    print("Creating tables...")
    print(Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)
    print("Tables created.")