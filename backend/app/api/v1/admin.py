from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import User
from app.core.dependencies import require_admin

from app.services.admin.admin_service import (
    get_admin_stats,
    get_all_users,
    get_usage_logs
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/stats")
def admin_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return get_admin_stats(db)


@router.get("/users")
def admin_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return get_all_users(db)


@router.get("/usage")
def admin_usage(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return get_usage_logs(db)