"""
Avesta Platform - Auction Model
"""

import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.config.database import Base


class Auction(Base):
    __tablename__ = "auctions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nft_id = Column(UUID(as_uuid=True), ForeignKey("nfts.id"))
    seller_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    start_price_ton = Column(Numeric(30, 8))
    current_bid_ton = Column(Numeric(30, 8), default=Decimal("0"))
    highest_bidder_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime)
    status = Column(String, default="Active")
    
    def __repr__(self):
        return f"<Auction {self.id}>"


class Offer(Base):
    __tablename__ = "offers"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nft_id = Column(UUID(as_uuid=True), ForeignKey("nfts.id"))
    buyer_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    offer_price_ton = Column(Numeric(30, 8))
    status = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)
