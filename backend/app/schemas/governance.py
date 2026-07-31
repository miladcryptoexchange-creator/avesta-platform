"""
Avesta Platform - Governance Schemas
"""

from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from decimal import Decimal
from datetime import datetime


class ProposalCreate(BaseModel):
    title: str
    description: str
    category: str


class ProposalResponse(BaseModel):
    id: UUID
    title: str
    description: str
    category: str
    status: str
    yes_votes: Decimal
    no_votes: Decimal
    created_at: datetime
    
    class Config:
        from_attributes = True


class VoteRequest(BaseModel):
    proposal_id: UUID
    choice: str  # YES, NO, ABSTAIN
