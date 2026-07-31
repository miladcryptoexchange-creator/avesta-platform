"""
Avesta Platform - NFT API
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from decimal import Decimal
import uuid

from app.config.database import get_db
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.nft import NFT, NFTCollection, NFTAttribute
from app.schemas.nft import NFTResponse, NFTCreateRequest

router = APIRouter()


@router.get("/")
async def list_nfts(db: Session = Depends(get_db)):
    return db.query(NFT).filter(NFT.status == "Listed").all()


@router.get("/{nft_id}")
async def get_nft(nft_id: str, db: Session = Depends(get_db)):
    nft = db.query(NFT).filter(NFT.id == nft_id).first()
    if not nft:
        raise HTTPException(status_code=404, detail="NFT not found")
    return nft


@router.post("/create")
async def create_nft(data: NFTCreateRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    nft = NFT(
        id=uuid.uuid4(),
        token_id=f"AVN-NFT-{uuid.uuid4().hex[:8]}",
        name=data.name,
        description=data.description,
        collection_id=data.collection_id,
        creator_id=current_user.id,
        owner_id=current_user.id,
        rarity=data.rarity,
        status="Minted"
    )
    
    db.add(nft)
    db.commit()
    
    return {"success": True, "nft_id": str(nft.id)}
