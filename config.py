import os

TELEGRAM_TOKEN2 = os.environ.get('TELEGRAM_TOKEN2', '')
CHAT_ID2 = os.environ.get('CHAT_ID2', '')

if not TELEGRAM_TOKEN2 or not CHAT_ID2:
  raise Exception('TELEGRAM_TOKEN, CHAT_ID 확인필요')

if __name__ == "__main__":
  print(TELEGRAM_TOKEN2)
  print(CHAT_ID2)