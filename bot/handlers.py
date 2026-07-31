"""
Avesta Platform - Bot Message Handlers
"""

from telegram import Update
from telegram.ext import ContextTypes


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages."""
    text = update.message.text.lower()
    
    if 'hello' in text or 'hi' in text:
        await update.message.reply_text("Hello! Welcome to Avesta Platform!")
    elif 'balance' in text:
        await update.message.reply_text("Your AVN Balance: 0.00000000")
    else:
        await update.message.reply_text("I didn't understand. Use /help for commands.")


async def handle_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors."""
    print(f"Error: {context.error}")
    if update and update.effective_message:
        await update.effective_message.reply_text("An error occurred. Please try again.")
