"""
Avesta Platform - Wallet Model
"""

import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.database import Base


class Wallet(Base):
    __tablename__ = "wallets"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True)
    address = Column(String, unique=True, index=True)
    balance = Column(Numeric(30, 8), default=Decimal("0"))
    locked_balance = Column(Numeric(30, 8), default=Decimal("0"))
    status = Column(String, default="active")
    ton_address = Column(String, nullable=True)
    ton_balance = Column(Numeric(30, 8), default=Decimal("0"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="wallet")
    transactions = relationship("WalletTransaction", back_populates="wallet")
    
    def __repr__(self):
        return f"<Wallet {self.address}>"
