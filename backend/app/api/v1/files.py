from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import User
from app.core.dependencies import get_current_user
from app.services.file.file_service import upload_document


router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.post("/upload")
def upload_file(
    conversation_id: int | None = None,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return upload_document(
        conversation_id=conversation_id,
        file=file,
        db=db,
        current_user=current_user
    )