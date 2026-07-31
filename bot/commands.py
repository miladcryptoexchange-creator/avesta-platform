"""
Avesta Platform - Bot Commands
"""

COMMANDS = {
    'start': {
        'description': 'Start the bot and create account',
        'handler': 'start'
    },
    'wallet': {
        'description': 'Show AVN wallet balance',
        'handler': 'wallet_command'
    },
    'mining': {
        'description': 'Show mining status',
        'handler': 'mining_command'
    },
    'referral': {
        'description': 'Show referral link',
        'handler': 'referral_command'
    },
    'help': {
        'description': 'Show help message',
        'handler': '
        'help_command'
    }
}
