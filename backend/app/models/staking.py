"""
Avesta Platform - Staking Model
"""

import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.database import Base


class StakingPlan(Base):
    __tablename__ = "staking_plans"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    duration_days = Column(Integer)
    apy = Column(Numeric(30, 8))
    minimum_amount = Column(Numeric(30, 8))
    status = Column(String, default="active")
    created_at = Column(DateTime, default=datetime.utcnow)


class Stake(Base):
    __tablename__ = "stakes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    plan_id = Column(UUID(as_uuid=True), ForeignKey("staking_plans.id"))
    amount = Column(Numeric(30, 8))
    reward = Column(Numeric(30, 8), default=Decimal("0"))
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime)
    status = Column(String, default="ACTIVE")
    
    user = relationship("User", back_populates="stakes")
    
    def __repr__(self):
        return f"<Stake {self.id}>"


class StakingReward(Base):
    __tablename__ = "staking_rewards"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stake_id = Column(UUID(as_uuid=True), ForeignKey("stakes.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    amount = Column(Numeric(30, 8))
    claimed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
