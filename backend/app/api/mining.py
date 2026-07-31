"""
Avesta Platform - Mining API
Includes: Mining Sessions, Ads Boost, Lucky Spin
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from decimal import Decimal
import random

from app.config.database import get_db
from app.config.settings import get_settings
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.mining import MiningSession, MiningSettings
from app.models.wallet import Wallet
from app.models.transaction import Transaction
import uuid

router = APIRouter()
settings = get_settings()


@router.post("/start")
async def start_mining(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Start mining session."""
    # Check if active session exists
    active = db.query(MiningSession).filter(
        MiningSession.user_id == current_user.id,
        MiningSession.status == "ACTIVE"
    ).first()

    if active:
        raise HTTPException(status_code=400, detail="Active mining session exists")

    # Create session
    session = MiningSession(
        id=uuid.uuid4(),
        user_id=current_user.id,
        start_time=datetime.utcnow(),
        end_time=datetime.utcnow() + timedelta(hours=24),
        mining_rate=Decimal("0.25"),
        estimated_reward=Decimal("6.0"),
        status="ACTIVE"
    )

    db.add(session)
    db.commit()

    return {
        "success": True,
        "session_id": str(session.id),
        "start_time": session.start_time,
        "end_time": session.end_time,
        "mining_rate": float(session.mining_rate),
        "estimated_reward": float(session.estimated_reward)
    }


@router.get("/status")
async def mining_status(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get mining status."""
    session = db.query(MiningSession).filter(
        MiningSession.user_id == current_user.id,
        MiningSession.status.in_(["ACTIVE", "COMPLETED"])
    ).order_by(MiningSession.created_at.desc()).first()

    if not session:
        return {"active": False, "message": "No active session"}

    now = datetime.utcnow()
    if session.status == "ACTIVE" and now >= session.end_time:
        session.status = "COMPLETED"
        db.commit()

    remaining = max(0, (session.end_time - now).total_seconds()) if session.status == "ACTIVE" else 0

    return {
        "active": session.status == "ACTIVE",
        "status": session.status,
        "remaining_seconds": int(remaining),
        "remaining_time": str(timedelta(seconds=int(remaining))),
        "mining_rate": float(session.mining_rate),
        "estimated_reward": float(session.estimated_reward),
        "can_claim": session.status == "COMPLETED" and not session.claimed
    }


@router.post("/claim")
async def claim_reward(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Claim mining reward."""
    session = db.query(MiningSession).filter(
        MiningSession.user_id == current_user.id,
        MiningSession.status == "COMPLETED",
        MiningSession.claimed == False
    ).first()

    if not session:
        raise HTTPException(status_code=400, detail="No reward to claim")

    # Get wallet
    wallet = db.query(Wallet).filter(Wallet.user_id == current_user.id).first()
    if not wallet:
        raise HTTPException(status_code=400, detail="Wallet not found")

    # Calculate reward
    reward = session.estimated_reward

    # Add to wallet
    wallet.balance += reward
    session.claimed = True
    session.claimed_at = datetime.utcnow()

    # Create transaction
    tx = Transaction(
        id=uuid.uuid4(),
        tx_hash=f"MINE-{uuid.uuid4().hex[:16]}",
        sender_id=None,
        receiver_id=current_user.id,
        amount=reward,
        tx_type="MINING_REWARD",
        status="CONFIRMED"
    )

    db.add(tx)
    db.commit()

    return {
        "success": True,
        "reward": float(reward),
        "new_balance": float(wallet.balance),
        "message": "Mining reward claimed successfully!"
    }


# ========== ADS BOOST SYSTEM ==========

@router.post("/boost")
async def watch_ad_boost(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Watch ad to boost mining rate (+2%). Max 5 ads per day = 10% boost."""
    session = db.query(MiningSession).filter(
        MiningSession.user_id == current_user.id,
        MiningSession.status == "ACTIVE"
    ).first()

    if not session:
        raise HTTPException(status_code=400, detail="No active mining session")

    # Check daily limit (5 ads)
    today = datetime.utcnow().date()
    daily_ads = db.query(MiningSession).filter(
        MiningSession.user_id == current_user.id,
        MiningSession.created_at >= today
    ).count()

    if daily_ads >= 5:
        raise HTTPException(status_code=400, detail="Daily ad limit reached (5/5)")

    # Apply boost (+2%)
    current_rate = float(session.mining_rate)
    boost_multiplier = 1.02
    new_rate = Decimal(str(current_rate * boost_multiplier))

    session.mining_rate = new_rate
    session.estimated_reward = new_rate * Decimal("24")

    db.commit()

    return {
        "success": True,
        "boost_applied": "2%",
        "new_mining_rate": float(new_rate),
        "new_estimated_reward": float(session.estimated_reward),
        "ads_watched_today": daily_ads + 1,
        "message": "Ad watched! Mining rate boosted by 2%"
    }


# ========== LUCKY SPIN SYSTEM ==========

SPIN_REWARDS = [
    {"reward": "1 AVN", "amount": Decimal("1"), "chance": 40},
    {"reward": "5 AVN", "amount": Decimal("5"), "chance": 20},
    {"reward": "10 AVN", "amount": Decimal("10"), "chance": 10},
    {"reward": "50 XP", "amount": Decimal("0"), "xp": 50, "chance": 15},
    {"reward": "Badge", "amount": Decimal("0"), "badge": "Lucky Spinner", "chance": 8},
    {"reward": "Mystery Box", "amount": Decimal("0"), "mystery": True, "chance": 5},
    {"reward": "100 AVN", "amount": Decimal("100"), "chance": 2},
]


@router.post("/spin")
async def lucky_spin(
    use_ad: bool = False,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Lucky Spin - 2 free spins daily, 3 more with ads."""

    # Check spins used today
    today = datetime.utcnow().date()
    # TODO: Implement spin tracking in database
    spins_used = 0  # Placeholder

    free_spins = 2
    max_ad_spins = 3

    if spins_used < free_spins:
        spin_type = "free"
    elif use_ad and spins_used < free_spins + max_ad_spins:
        spin_type = "ad"
    else:
        raise HTTPException(status_code=400, detail="No spins remaining today")

    # Weighted random selection
    total_chance = sum(r["chance"] for r in SPIN_REWARDS)
    rand = random.randint(1, total_chance)

    cumulative = 0
    selected = SPIN_REWARDS[0]
    for reward in SPIN_REWARDS:
        cumulative += reward["chance"]
        if rand <= cumulative:
            selected = reward
            break

    # Apply reward
    result = {
        "spin_type": spin_type,
        "reward_name": selected["reward"],
        "reward_applied": False
    }

    if selected["amount"] > 0:
        wallet = db.query(Wallet).filter(Wallet.user_id == current_user.id).first()
        if wallet:
            wallet.balance += selected["amount"]
            result["reward_applied"] = True
            result["avn_amount"] = float(selected["amount"])

    if "xp" in selected:
        current_user.xp += selected["xp"]
        result["xp_gained"] = selected["xp"]
        result["reward_applied"] = True

    db.commit()

    return result
