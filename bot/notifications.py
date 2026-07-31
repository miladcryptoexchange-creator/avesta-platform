"""
Avesta Platform - Bot Notifications
"""

from telegram import Bot


async def send_mining_complete(bot: Bot, chat_id: int, reward: float):
    """Send mining completion notification."""
    await bot.send_message(
        chat_id=chat_id,
        text=f"Your mining session is complete!\nYou earned {reward} AVN."
    )


async def send_transaction_notification(bot: Bot, chat_id: int, amount: float):
    """Send transaction notification."""
    await bot.send_message(
        chat_id=chat_id,
        text=f"You received {amount} AVN!"
    )


async def send_referral_notification(bot: Bot, chat_id: int, username: str):
    """Send referral notification."""
    await bot.send_message(
        chat_id=chat_id,
        text=f"New user joined using your link: {username}"
    )
