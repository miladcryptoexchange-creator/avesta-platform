"""
Avesta Platform - TON API
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.wallet import Wallet

router = APIRouter()


@router.get("/balance/{wallet_address}")
async def get_ton_balance(wallet_address: str):
    # TODO: Integrate with TON API
    return {"wallet": wallet_address, "ton": "0", "status": "connected"}


@router.post("/connect")
async def connect_ton_wallet(ton_address: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    wallet = db.query(Wallet).filter(Wallet.user_id == current_user.id).first()
    if wallet:
        wallet.ton_address = ton_address
        db.commit()
    
    return {"success": True, "ton_address": ton_address}
