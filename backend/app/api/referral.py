"""
Avesta Platform - Referral API
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.config.database import get_db
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.referral import Referral, ReferralReward
from app.schemas.referral import ReferralResponse

router = APIRouter()


@router.get("/profile")
async def referral_profile(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    total_invites = db.query(Referral).filter(Referral.referrer_id == current_user.id).count()
    earned = db.query(func.sum(ReferralReward.amount)).filter(ReferralReward.user_id == current_user.id).scalar() or 0
    
    return {
        "referral_code": current_user.referral_code,
        "referral_link": f"https://t.me/AvestaBot?start={current_user.referral_code}",
        "total_invites": total_invites,
        "earned_avn": float(earned)
    }


@router.get("/leaderboard")
async def referral_leaderboard(db: Session = Depends(get_db)):
    # Top 50 referrers
    top = db.query(
        User.username,
        func.count(Referral.id).label("invites")
    ).join(Referral, User.id == Referral.referrer_id).group_by(User.id).order_by(func.count(Referral.id).desc()).limit(50).all()
    
    return [{"rank": i+1, "username": t.username, "invites": t.invites} for i, t in enumerate(top)]
