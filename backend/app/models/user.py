"""
Avesta Platform - User Model
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telegram_id = Column(String, unique=True, nullable=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    avatar = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    country = Column(String, nullable=True)
    referral_code = Column(String, unique=True, index=True)
    referred_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    level = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_creator = Column(Boolean, default=False)
    role = Column(String, default="user")
    wallet_address = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    
    wallet = relationship("Wallet", back_populates="user", uselist=False)
    transactions_sent = relationship("Transaction", foreign_keys="Transaction.sender_id", back_populates="sender")
    transactions_received = relationship("Transaction", foreign_keys="Transaction.receiver_id", back_populates="receiver")
    mining_sessions = relationship("MiningSession", back_populates="user")
    referrals = relationship("Referral", foreign_keys="Referral.referrer_id", back_populates="referrer")
    stakes = relationship("Stake", back_populates="user")
    votes = relationship("Vote", back_populates="user")
    nfts_created = relationship("NFT", foreign_keys="NFT.creator_id", back_populates="creator")
    nfts_owned = relationship("NFT", foreign_keys="NFT.owner_id", back_populates="owner")
    notifications = relationship("Notification", back_populates="user")
    
    def __repr__(self):
        return f"<User {self.username}>"
