from pathlib import Path
import shutil

from fastapi import UploadFile

from app.core.config import settings


def save_uploaded_file(
    file: UploadFile,
    file_id: int
) -> Path:
    """
    Save uploaded file to disk and return the saved path.
    """

    settings.UPLOAD_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    original_name = file.filename or "uploaded_file"

    safe_filename = original_name.replace(
        " ",
        "_"
    )

    file_path = (
        settings.UPLOAD_DIR
        / f"{file_id}_{safe_filename}"
    )

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return file_path