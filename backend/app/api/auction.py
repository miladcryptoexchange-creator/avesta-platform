"""
Avesta Platform - Auction API
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from decimal import Decimal
import uuid

from app.config.database import get_db
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.auction import Auction
from app.models.nft import NFT

router = APIRouter()


@router.post("/create")
async def create_auction(nft_id: str, start_price: float, duration_hours: int = 24, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    nft = db.query(NFT).filter(NFT.id == nft_id, NFT.owner_id == current_user.id).first()
    if not nft:
        raise HTTPException(status_code=404, detail="NFT not found")
    
    auction = Auction(
        id=uuid.uuid4(),
        nft_id=nft_id,
        seller_id=current_user.id,
        start_price_ton=Decimal(str(start_price)),
        end_time=datetime.utcnow() + timedelta(hours=duration_hours)
    )
    
    db.add(auction)
    db.commit()
    
    return {"success": True, "auction_id": str(auction.id)}


@router.get("/")
async def list_auctions(db: Session = Depends(get_db)):
    return db.query(Auction).filter(Auction.status == "Active").all()
