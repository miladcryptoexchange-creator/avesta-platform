"""
Avesta Platform - Referral Schemas
"""

from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
from datetime import datetime


class ReferralResponse(BaseModel):
    referral_code: str
    total_invites: int
    active_referrals: int
    earned_avn: Decimal
    referral_link: str
