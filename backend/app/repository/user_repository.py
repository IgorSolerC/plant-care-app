from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.auth.security import get_password_hash

def get_by_email(db: Session, *, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def create(db: Session, *, user_in: UserCreate) -> User:
    hashed_password = get_password_hash(user_in.password)
    db_user = User(
        email=user_in.email,
        hashed_password=hashed_password,
        full_name=user_in.full_name
    )
    db.add(db_user)
    return db_user

def create_from_google(db: Session, *, email: str, full_name: str | None, google_id: str) -> User:
    db_user = User(
        email=email,
        full_name=full_name,
        google_id=google_id,
        hashed_password=None,
        is_active=True
    )
    db.add(db_user)
    return db_user

def link_google_account(db: Session, *, user: User, google_id: str) -> User:
    user.google_id = google_id
    db.add(user)
    return user