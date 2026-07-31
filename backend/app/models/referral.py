"""
Avesta Platform - Referral Model
"""

import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.database import Base


class Referral(Base):
    __tablename__ = "referrals"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    referrer_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    referred_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    level = Column(Integer, default=1)
    reward_amount = Column(Numeric(30, 8), default=Decimal("0"))
    status = Column(String, default="active")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    referrer = relationship("User", foreign_keys=[referrer_id], back_populates="referrals")
    
    def __repr__(self):
        return f"<Referral {self.id}>"


class ReferralReward(Base):
    __tablename__ = "referral_rewards"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    source_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    amount = Column(Numeric(30, 8))
    level = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
