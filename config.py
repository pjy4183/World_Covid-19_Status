import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN2','')
CHAT_ID = os.environ.get('CHAT_ID2','')

if not TELEGRAM_TOKEN or not CHAT_ID:
    raise Exception('TELEGRAM_TOKEN or CHAT_ID needs to be checked')