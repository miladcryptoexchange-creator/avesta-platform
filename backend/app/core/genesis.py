"""
Avesta Platform - Genesis Block & Supply Management
"""

from decimal import Decimal
from sqlalchemy.orm import Session
from app.models.block import Block
from app.models.transaction import Transaction

GENESIS_SUPPLY = Decimal("21000000000")

TOKENOMICS = {
    "mining_rewards": Decimal("9450000000"),
    "community_referral": Decimal("2100000000"),
    "liquidity_exchange": Decimal("2100000000"),
    "team": Decimal("2100000000"),
    "treasury": Decimal("2100000000"),
    "marketing": Decimal("1470000000"),
    "ecosystem": Decimal("1680000000"),
}


class GenesisManager:
    @staticmethod
    def create_genesis_block(db: Session) -> Block:
        genesis = Block(
            block_number=0,
            previous_hash="0" * 64,
            hash="0" * 64,
            nonce=0,
            data={
                "name": "Avesta Platform",
                "symbol": "AVN",
                "total_supply": str(GENESIS_SUPPLY),
                "tokenomics": {k: str(v) for k, v in TOKENOMICS.items()},
                "message": "Genesis Block of Avesta Blockchain"
            },
            transaction_count=0
        )
        db.add(genesis)
        db.commit()
        db.refresh(genesis)
        return genesis

    @staticmethod
    def get_total_supply() -> Decimal:
        return GENESIS_SUPPLY

    @staticmethod
    def get_circulating_supply(db: Session) -> Decimal:
        return GENESIS_SUPPLY

    @staticmethod
    def allocate_from_genesis(amount: Decimal) -> bool:
        return True
