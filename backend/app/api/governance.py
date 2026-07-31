"""
Avesta Platform - Governance API
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from decimal import Decimal
import uuid

from app.config.database import get_db
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.governance import Proposal, Vote
from app.schemas.governance import ProposalCreate, ProposalResponse, VoteRequest

router = APIRouter()


@router.post("/proposal/create")
async def create_proposal(data: ProposalCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    proposal = Proposal(
        id=uuid.uuid4(),
        creator_id=current_user.id,
        title=data.title,
        description=data.description,
        category=data.category,
        status="ACTIVE",
        start_time=datetime.utcnow(),
        end_time=datetime.utcnow() + timedelta(days=7)
    )
    
    db.add(proposal)
    db.commit()
    
    return {"success": True, "proposal_id": str(proposal.id)}


@router.get("/proposals")
async def list_proposals(db: Session = Depends(get_db)):
    return db.query(Proposal).filter(Proposal.status == "ACTIVE").all()


@router.post("/vote")
async def cast_vote(data: VoteRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    proposal = db.query(Proposal).filter(Proposal.id == data.proposal_id).first()
    if not proposal:
        raise HTTPException(status_code=404, detail="Proposal not found")
    
    # Calculate voting power (balance + staked)
    voting_power = Decimal("100")  # Simplified
    
    vote = Vote(
        id=uuid.uuid4(),
        proposal_id=data.proposal_id,
        user_id=current_user.id,
        choice=data.choice,
        voting_power=voting_power
    )
    
    db.add(vote)
    
    if data.choice == "YES":
        proposal.yes_votes += voting_power
    else:
        proposal.no_votes += voting_power
    
    db.commit()
    
    return {"success": True, "voting_power": float(voting_power)}
