import telegram
import telebot
import time
import random
import asyncio
import aiohttp
import requests
import platform

# Замените YOUR_TOKEN на токен вашего бота
bot = telebot.TeleBot(token="")
# bot.infinity_polling(timeout=5, long_polling_timeout=5)

# Список эмодзи
emojis = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🤎", "🤍", "💕", "💞", "💖", "💖"]
words = [
    "крошка",
    "принцесска",
    "милая",
    "дорогая",
    "ласковая",
    "очаровашка",
    "жемчужинка",
    "прекрасная",
    "великолепная",
    "обворожительная",
]


async def func():
    # Отправляем случайный эмодзи
    try:
        bot.send_message(
            chat_id="-1001678389024",
            text="name " + random.choice(words) + random.choice(emojis),
        )
    except:
        time.sleep(5)
        bot.send_message(
            chat_id="-1001678389024",
            text="name " + random.choice(words) + random.choice(emojis),
        )


while True:

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(func())
    time.sleep(5)
