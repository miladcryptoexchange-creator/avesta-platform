"""
Avesta Platform - Telegram Bot
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Bot token (set via environment variable)
BOT_TOKEN = "YOUR_BOT_TOKEN"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler."""
    user = update.effective_user
    
    keyboard = [
        [InlineKeyboardButton("Open Avesta App", web_app={"url": "https://your-domain.com/telegram-mini-app"})],
        [InlineKeyboardButton("Wallet", callback_data='wallet')],
        [InlineKeyboardButton("Mining", callback_data='mining')],
        [InlineKeyboardButton("Referral", callback_data='referral')]
    ]
    
    await update.message.reply_text(
        f"Welcome to Avesta Platform!\n\n"
        f"Your Web3 journey starts here.\n"
        f"Your AVN Wallet has been created.\n\n"
        f"User: {user.first_name}",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command handler."""
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/wallet - Show AVN balance\n"
        "/mining - Show mining status\n"
        "/referral - Show referral link\n"
        "/help - Show this help message"
    )


async def wallet_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Wallet command handler."""
    await update.message.reply_text(
        "AVN Wallet\n\n"
        "Balance: 0.00000000 AVN\n"
        "Address: AVN-XXXXXXXX"
    )


async def mining_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mining command handler."""
    await update.message.reply_text(
        "Mining Status\n\n"
        "Status: Inactive\n"
        "Click 'Open Avesta App' to start mining!"
    )


async def referral_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Referral command handler."""
    user_id = update.effective_user.id
    await update.message.reply_text(
        "Your Referral Link\n\n"
        f"https://t.me/AvestaBot?start={user_id}\n\n"
        "Invite friends and earn 10% of their mining rewards!"
    )


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Button callback handler."""
    query = update.callback_query
    await query.answer()
    
    if query.data == 'wallet':
        await query.edit_message_text("AVN Balance: 0.00000000")
    elif query.data == 'mining':
        await query.edit_message_text("Mining: Start from the Mini App")


def main():
    """Start the bot."""
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("wallet", wallet_command))
    application.add_handler(CommandHandler("mining", mining_command))
    application.add_handler(CommandHandler("referral", referral_command))
    
    # Callback handler
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Run the bot
    application.run_polling()


if __name__ == '__main__':
    main()
