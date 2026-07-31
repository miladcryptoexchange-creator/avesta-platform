"""
Avesta Platform - Main Application
FastAPI Backend Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config.database import init_db
from app.api import auth, users, wallet, mining, transaction, referral, governance, staking, admin, nft, marketplace, auction, ton, blockchain, telegram, ai


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    print("Avesta Platform started!")
    yield
    print("Shutting down...")


app = FastAPI(
    title="Avesta Platform API",
    description="Web3 Ecosystem with AVN Token",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(wallet.router, prefix="/api/wallet", tags=["Wallet"])
app.include_router(mining.router, prefix="/api/mining", tags=["Mining"])
app.include_router(transaction.router, prefix="/api/transaction", tags=["Transaction"])
app.include_router(referral.router, prefix="/api/referral", tags=["Referral"])
app.include_router(governance.router, prefix="/api/governance", tags=["Governance"])
app.include_router(staking.router, prefix="/api/staking", tags=["Staking"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])
app.include_router(nft.router, prefix="/api/nft", tags=["NFT"])
app.include_router(marketplace.router, prefix="/api/marketplace", tags=["Marketplace"])
app.include_router(auction.router, prefix="/api/auction", tags=["Auction"])
app.include_router(ton.router, prefix="/api/ton", tags=["TON"])
app.include_router(blockchain.router, prefix="/api/blockchain", tags=["Blockchain"])
app.include_router(telegram.router, prefix="/api/telegram", tags=["Telegram"])
app.include_router(ai.router, prefix="/api/ai", tags=["AI"])


@app.get("/")
async def root():
    return {"project": "Avesta Platform", "version": "1.0.0", "status": "running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
