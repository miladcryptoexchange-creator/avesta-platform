"""
Avesta Platform - Wallet API
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from decimal import Decimal
import uuid

from app.config.database import get_db
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.wallet import Wallet
from app.models.transaction import Transaction
from app.schemas.wallet import WalletResponse, TransferRequest

router = APIRouter()


@router.get("/", response_model=WalletResponse)
async def get_wallet(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    wallet = db.query(Wallet).filter(Wallet.user_id == current_user.id).first()
    if not wallet:
        wallet = Wallet(
            id=uuid.uuid4(),
            user_id=current_user.id,
            address=f"AVN-{uuid.uuid4().hex[:8].upper()}",
            balance=Decimal("0"),
            status="active"
        )
        db.add(wallet)
        db.commit()
        db.refresh(wallet)
    return wallet


@router.post("/transfer")
async def transfer_avn(data: TransferRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    amount = data.amount
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")
    
    sender_wallet = db.query(Wallet).filter(Wallet.user_id == current_user.id).first()
    if not sender_wallet or sender_wallet.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    receiver_wallet = db.query(Wallet).filter(Wallet.address == data.receiver_address).first()
    if not receiver_wallet:
        raise HTTPException(status_code=404, detail="Receiver wallet not found")
    
    sender_wallet.balance -= amount
    receiver_wallet.balance += amount
    
    tx = Transaction(
        id=uuid.uuid4(),
        tx_hash=f"TX-{uuid.uuid4().hex[:16]}",
        sender_id=current_user.id,
        receiver_id=receiver_wallet.user_id,
        amount=amount,
        tx_type="TRANSFER",
        status="CONFIRMED"
    )
    
    db.add(tx)
    db.commit()
    
    return {
        "success": True,
        "tx_hash": tx.tx_hash,
        "amount": float(amount),
        "new_balance": float(sender_wallet.balance)
    }


@router.get("/history")
async def wallet_history(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    transactions = db.query(Transaction).filter(
        (Transaction.sender_id == current_user.id) | (Transaction.receiver_id == current_user.id)
    ).order_by(Transaction.created_at.desc()).limit(50).all()
    
    return [{
        "tx_hash": tx.tx_hash,
        "type": tx.tx_type,
        "amount": float(tx.amount),
        "status": tx.status,
        "created_at": tx.created_at
    } for tx in transactions]
