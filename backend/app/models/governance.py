"""
Avesta Platform - Governance Model
"""

import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, Integer, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.database import Base


class Proposal(Base):
    __tablename__ = "proposals"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    title = Column(String)
    description = Column(Text)
    category = Column(String)
    status = Column(String, default="DRAFT")
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    yes_votes = Column(Numeric(30, 8), default=Decimal("0"))
    no_votes = Column(Numeric(30, 8), default=Decimal("0"))
    quorum = Column(Numeric(30, 8), default=Decimal("0"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    votes = relationship("Vote", back_populates="proposal")
    
    def __repr__(self):
        return f"<Proposal {self.title}>"


class Vote(Base):
    __tablename__ = "votes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    proposal_id = Column(UUID(as_uuid=True), ForeignKey("proposals.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    choice = Column(String)  # YES, NO, ABSTAIN
    voting_power = Column(Numeric(30, 8))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    proposal = relationship("Proposal", back_populates="votes")
    user = relationship("User", back_populates="votes")
    
    def __repr__(self):
        return f"<Vote {self.id}>"


class DAOTreasury(Base):
    __tablename__ = "dao_treasury"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    balance = Column(Numeric(30, 8), default=Decimal("0"))
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
