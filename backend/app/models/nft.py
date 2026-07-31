"""
Avesta Platform - NFT Model
"""

import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.database import Base


class NFTCollection(Base):
    __tablename__ = "collections"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    name = Column(String)
    symbol = Column(String)
    description = Column(Text)
    logo_url = Column(String)
    banner_url = Column(String)
    category = Column(String)
    total_supply = Column(Integer)
    minted_count = Column(Integer, default=0)
    floor_price_ton = Column(Numeric(30, 8), default=Decimal("0"))
    royalty_percentage = Column(Numeric(30, 8), default=Decimal("5"))
    verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    nfts = relationship("NFT", back_populates="collection")
    
    def __repr__(self):
        return f"<Collection {self.name}>"


class NFT(Base):
    __tablename__ = "nfts"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    token_id = Column(String, unique=True)
    name = Column(String)
    description = Column(Text)
    image_url = Column(String)
    metadata_url = Column(String)
    collection_id = Column(UUID(as_uuid=True), ForeignKey("collections.id"))
    creator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    rarity = Column(String)
    rarity_score = Column(Numeric(30, 8))
    price_ton = Column(Numeric(30, 8), default=Decimal("0"))
    status = Column(String, default="Minted")
    mint_transaction_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    collection = relationship("NFTCollection", back_populates="nfts")
    creator = relationship("User", foreign_keys=[creator_id], back_populates="nfts_created")
    owner = relationship("User", foreign_keys=[owner_id], back_populates="nfts_owned")
    attributes = relationship("NFTAttribute", back_populates="nft")
    
    def __repr__(self):
        return f"<NFT {self.name}>"


class NFTAttribute(Base):
    __tablename__ = "nft_attributes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nft_id = Column(UUID(as_uuid=True), ForeignKey("nfts.id"))
    trait_type = Column(String)
    value = Column(String)
    rarity_percentage = Column(Numeric(30, 8))
    
    nft = relationship("NFT", back_populates="attributes")
