"""
Avesta Platform - Mining Session Model
"""

import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.database import Base


class MiningSession(Base):
    __tablename__ = "mining_sessions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime)
    duration = Column(Integer, default=24)
    mining_rate = Column(Numeric(30, 8), default=Decimal("0.25"))
    estimated_reward = Column(Numeric(30, 8))
    actual_reward = Column(Numeric(30, 8), default=Decimal("0"))
    status = Column(String, default="ACTIVE")
    claimed = Column(Boolean, default=False)
    claimed_at = Column(DateTime, nullable=True)
    device_fingerprint = Column(String, nullable=True)
    ip_address = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="mining_sessions")
    
    def __repr__(self):
        return f"<MiningSession {self.id}>"


class MiningSettings(Base):
    __tablename__ = "mining_settings"
    
    id = Column(Integer, primary_key=True)
    base_rate = Column(Numeric(30, 8), default=Decimal("0.25"))
    cycle_hours = Column(Integer, default=24)
    max_reward = Column(Numeric(30, 8), default=Decimal("6"))
    referral_bonus_percent = Column(Numeric(30, 8), default=Decimal("10"))
    is_active = Column(Boolean, default=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
