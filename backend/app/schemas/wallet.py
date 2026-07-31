"""
Avesta Platform - Wallet Schemas
"""

from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from decimal import Decimal


class WalletResponse(BaseModel):
    address: str
    balance: Decimal
    locked_balance: Decimal
    ton_address: Optional[str]
    ton_balance: Decimal
    status: str
    
    class Config:
        from_attributes = True


class TransferRequest(BaseModel):
    receiver_address: str
    amount: Decimal
