"""
Avesta Platform - Blockchain API
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.models.block import Block

router = APIRouter()


@router.get("/blocks")
async def get_blocks(db: Session = Depends(get_db)):
    return db.query(Block).order_by(Block.block_number.desc()).limit(50).all()


@router.get("/latest")
async def get_latest_block(db: Session = Depends(get_db)):
    return db.query(Block).order_by(Block.block_number.desc()).first()


@router.get("/supply")
async def get_supply():
    from app.core.genesis import GENESIS_SUPPLY
    return {
        "total_supply": float(GENESIS_SUPPLY),
        "symbol": "AVN",
        "decimals": 9
    }
