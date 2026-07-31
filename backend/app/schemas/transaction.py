"""
Avesta Platform - Transaction Schemas
"""

from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from decimal import Decimal
from datetime import datetime


class TransactionResponse(BaseModel):
    tx_hash: str
    tx_type: str
    amount: Decimal
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
