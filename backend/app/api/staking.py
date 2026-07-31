"""
Avesta Platform - Staking API
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from decimal import Decimal
import uuid

from app.config.database import get_db
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.staking import StakingPlan, Stake, StakingReward
from app.models.wallet import Wallet

router = APIRouter()


@router.get("/plans")
async def get_plans(db: Session = Depends(get_db)):
    return db.query(StakingPlan).filter(StakingPlan.status == "active").all()


@router.post("/create")
async def create_stake(plan_id: str, amount: float, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    plan = db.query(StakingPlan).filter(StakingPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    wallet = db.query(Wallet).filter(Wallet.user_id == current_user.id).first()
    if not wallet or wallet.balance < Decimal(str(amount)):
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    wallet.balance -= Decimal(str(amount))
    
    stake = Stake(
        id=uuid.uuid4(),
        user_id=current_user.id,
        plan_id=plan.id,
        amount=Decimal(str(amount)),
        end_date=datetime.utcnow() + timedelta(days=plan.duration_days)
    )
    
    db.add(stake)
    db.commit()
    
    return {"success": True, "stake_id": str(stake.id)}


@router.get("/my-stakes")
async def my_stakes(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return db.query(Stake).filter(Stake.user_id == current_user.id).all()
