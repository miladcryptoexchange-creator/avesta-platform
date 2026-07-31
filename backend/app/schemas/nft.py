"""
Avesta Platform - NFT Schemas
"""

from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from decimal import Decimal
from datetime import datetime


class NFTAttributeResponse(BaseModel):
    trait_type: str
    value: str
    rarity_percentage: Decimal


class NFTResponse(BaseModel):
    id: UUID
    name: str
    image_url: str
    rarity: str
    price_ton: Decimal
    status: str
    created_at: datetime
    attributes: List[NFTAttributeResponse]
    
    class Config:
        from_attributes = True


class NFTCreateRequest(BaseModel):
    name: str
    description: str
    collection_id: UUID
    rarity: str
