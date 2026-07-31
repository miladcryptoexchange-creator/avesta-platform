"""
Avesta Platform - Transaction API
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionResponse

router = APIRouter()


@router.get("/", response_model=List[TransactionResponse])
async def list_transactions(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return db.query(Transaction).filter(
        (Transaction.sender_id == current_user.id) | (Transaction.receiver_id == current_user.id)
    ).order_by(Transaction.created_at.desc()).all()


@router.get("/{tx_hash}")
async def get_transaction(tx_hash: str, db: Session = Depends(get_db)):
    tx = db.query(Transaction).filter(Transaction.tx_hash == tx_hash).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx
