from sqlalchemy.orm import Session
from app.models.user import User
from datetime import datetime, UTC
from app.core.security import hash_password, verify_password, create_access_token


def register_user(db: Session, email: str, password: str, role:str ,name: str | None = None):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        return None

    user = User(
        name=name,
        email=email,
        role=role,
        password_hash=hash_password(password),
        created_at=datetime.now(UTC)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

from passlib.exc import UnknownHashError

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    try:
        password_valid = verify_password(password, user.password_hash)
    except UnknownHashError:
        password_valid = False

    if not password_valid:
        return None

    token = create_access_token({"sub": str(user.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }