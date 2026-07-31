"""
Avesta Platform - Marketplace API
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from decimal import Decimal

from app.config.database import get_db
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.nft import NFT
from app.models.wallet import Wallet

router = APIRouter()


@router.get("/listings")
async def get_listings(db: Session = Depends(get_db)):
    return db.query(NFT).filter(NFT.status == "Listed").all()


@router.post("/buy")
async def buy_nft(nft_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    nft = db.query(NFT).filter(NFT.id == nft_id, NFT.status == "Listed").first()
    if not nft:
        raise HTTPException(status_code=404, detail="NFT not found or not listed")
    
    buyer_wallet = db.query(Wallet).filter(Wallet.user_id == current_user.id).first()
    if not buyer_wallet or buyer_wallet.ton_balance < nft.price_ton:
        raise HTTPException(status_code=400, detail="Insufficient TON balance")
    
    # Transfer ownership
    seller_wallet = db.query(Wallet).filter(Wallet.user_id == nft.owner_id).first()
    
    buyer_wallet.ton_balance -= nft.price_ton
    seller_wallet.ton_balance += nft.price_ton
    
    nft.owner_id = current_user.id
    nft.status = "Sold"
    
    db.commit()
    
    return {"success": True, "message": "NFT purchased successfully"}
