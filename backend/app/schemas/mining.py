"""
Avesta Platform - Mining Schemas
"""

from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from decimal import Decimal
from datetime import datetime


class MiningStatusResponse(BaseModel):
    active: bool
    status: str
    remaining_seconds: int
    remaining_time: str
    mining_rate: Decimal
    estimated_reward: Decimal
    can_claim: bool


class MiningClaimResponse(BaseModel):
    success: bool
    reward: Decimal
    new_balance: Decimal
    message: str


class SpinResponse(BaseModel):
    spin_type: str
    reward_name: str
    reward_applied: bool
    avn_amount: Optional[Decimal] = None
    xp_gained: Optional[int] = None
