"""
This is a echo bot.
It echoes any incoming text messages.
"""

# import logging

from aiogram import Bot, Dispatcher, executor, types
from config import *
from user_info import router, profile_print

# API_TOKEN = '1806266195:AAGg7cBPmP16tWtqhIjDS-Dnq4R9xbrX2UE'

# Configure logging
# logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
from main_menu import main_menu


@dp.message_handler(commands=['start', 'help', 'about'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    print(message.text)
    user_id = message['from']['id']
    if message.text == 'Регистрация' or USERS.get(user_id) is None or USERS[user_id].WHERE_I_WAS != '' :
        await router(message)
    elif message.text == 'Профиль':
        await profile_print(message)
    else:
        await main_menu(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
