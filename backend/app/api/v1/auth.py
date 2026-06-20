from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import RegisterRequest, LoginRequest, TokenResponse
from app.services.auth.auth_service import register_user, login_user
from app.models import User
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(req: RegisterRequest, db: Session = Depends(get_db)):
    user = register_user(db, req.email, req.password, req.role, req.name)
    if not user:
        raise HTTPException(status_code=400, detail="User already exists")

    return {"message": "User registered successfully", "email": user.email}


@router.post("/login", response_model=TokenResponse)
def login(
    req: LoginRequest,
    db: Session = Depends(get_db)
):
    token = login_user(db, req.email, req.password)
    
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return token

@router.get("/me")
def me(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role
    }