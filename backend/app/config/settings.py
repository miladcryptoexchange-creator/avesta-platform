"""
Avesta Platform - Core Configuration
"""

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = "Avesta Platform"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/avesta"
    REDIS_URL: str = "redis://localhost:6379/0"
    SECRET_KEY: str = "avesta-secret-key-2024"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080
    GENESIS_SUPPLY: int = 21_000_000_000
    MINING_REWARD_PERCENT: float = 45.0
    COMMUNITY_REFERRAL_PERCENT: float = 10.0
    LIQUIDITY_EXCHANGE_PERCENT: float = 10.0
    TEAM_PERCENT: float = 10.0
    TREASURY_PERCENT: float = 10.0
    MARKETING_PERCENT: float = 7.0
    ECOSYSTEM_DEVELOPMENT_PERCENT: float = 8.0
    MINING_DURATION_HOURS: int = 24
    BASE_MINING_RATE: float = 0.25
    REFERRAL_LEVEL_1_PERCENT: float = 10.0
    REFERRAL_LEVEL_2_PERCENT: float = 5.0
    REFERRAL_LEVEL_3_PERCENT: float = 2.0
    TON_API_KEY: str = ""
    TON_NETWORK: str = "testnet"
    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_WEBHOOK_URL: str = ""
    AI_IMAGE_API_KEY: str = ""
    AI_IMAGE_PROVIDER: str = "stability"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
