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

router = APIRouter()


@router.get("/")
async def get_wallet(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get user wallet."""
    wallet = db.query(Wallet).filter(Wallet.user_id == current_user.id).first()
    if not wallet:
        # Auto-create wallet
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

    return {
        "address": wallet.address,
        "balance": float(wallet.balance),
        "locked_balance": float(wallet.locked_balance),
        "ton_address": wallet.ton_address,
        "ton_balance": float(wallet.ton_balance) if wallet.ton_balance else 0,
        "status": wallet.status
    }


@router.post("/transfer")
async def transfer_avn(
    receiver_address: str,
    amount: float,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Transfer AVN to another wallet."""
    amount_decimal = Decimal(str(amount))

    if amount_decimal <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")

    # Get sender wallet
    sender_wallet = db.query(Wallet).filter(Wallet.user_id == current_user.id).first()
    if not sender_wallet or sender_wallet.balance < amount_decimal:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    # Get receiver wallet
    receiver_wallet = db.query(Wallet).filter(Wallet.address == receiver_address).first()
    if not receiver_wallet:
        raise HTTPException(status_code=404, detail="Receiver wallet not found")

    # Transfer
    sender_wallet.balance -= amount_decimal
    receiver_wallet.balance += amount_decimal

    # Create transaction
    tx = Transaction(
        id=uuid.uuid4(),
        tx_hash=f"TX-{uuid.uuid4().hex[:16]}",
        sender_id=current_user.id,
        receiver_id=receiver_wallet.user_id,
        amount=amount_decimal,
        tx_type="TRANSFER",
        status="CONFIRMED"
    )

    db.add(tx)
    db.commit()

    return {
        "success": True,
        "tx_hash": tx.tx_hash,
        "amount": float(amount_decimal),
        "from": sender_wallet.address,
        "to": receiver_address,
        "new_balance": float(sender_wallet.balance)
    }


@router.get("/history")
async def wallet_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get wallet transaction history."""
    transactions = db.query(Transaction).filter(
        (Transaction.sender_id == current_user.id) | 
        (Transaction.receiver_id == current_user.id)
    ).order_by(Transaction.created_at.desc()).limit(50).all()

    return [{
        "tx_hash": tx.tx_hash,
        "type": tx.tx_type,
        "amount": float(tx.amount),
        "status": tx.status,
        "created_at": tx.created_at
    } for tx in transactions]
