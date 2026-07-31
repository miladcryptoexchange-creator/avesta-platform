"""
Avesta Platform - Bot Configuration
"""

import os

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN')
WEBHOOK_URL = os.getenv('TELEGRAM_WEBHOOK_URL', '')
API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:8000')
