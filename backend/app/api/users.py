"""
Avesta Platform - Users API
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.core.security import get_current_active_user
from app.models.user import User
from app.schemas.user import UserResponse

router = APIRouter()


@router.get("/", response_model=List[UserResponse])
async def list_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return db.query(User).all()


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
