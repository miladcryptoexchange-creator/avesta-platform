"""
Avesta Platform - Block Model
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.config.database import Base


class Block(Base):
    __tablename__ = "blocks"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    block_number = Column(Integer, unique=True, index=True)
    hash = Column(String, unique=True, index=True)
    previous_hash = Column(String, index=True)
    merkle_root = Column(String)
    nonce = Column(Integer, default=0)
    difficulty = Column(Integer, default=1)
    data = Column(JSON)
    transaction_count = Column(Integer, default=0)
    timestamp = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Block #{self.block_number}>"
