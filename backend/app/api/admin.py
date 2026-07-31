"""
Avesta Platform - Admin API
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.config.database import get_db
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.wallet import Wallet
from app.models.transaction import Transaction
from app.models.mining import MiningSession

router = APIRouter()


@router.get("/dashboard")
async def admin_dashboard(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    
    total_users = db.query(func.count(User.id)).scalar()
    total_wallets = db.query(func.count(Wallet.id)).scalar()
    total_transactions = db.query(func.count(Transaction.id)).scalar()
    active_miners = db.query(func.count(MiningSession.id)).filter(MiningSession.status == "ACTIVE").scalar()
    
    return {
        "total_users": total_users,
        "total_wallets": total_wallets,
        "total_transactions": total_transactions,
        "active_miners": active_miners
    }


@router.get("/users")
async def list_all_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    
    return db.query(User).all()
