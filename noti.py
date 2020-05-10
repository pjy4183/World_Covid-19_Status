from config import TELEGRAM_TOKEN2, CHAT_ID2
import requests as rq
import telegram

bot = telegram.Bot(token = TELEGRAM_TOKEN2)

def send(t):
    bot.sendMessage(CHAT_ID2, t, parse_mode=telegram.ParseMode.HTML)