from User import User
from config import *
from main_menu import main_menu
async def router(message: types.Message):
    user_id = message['from']['id']
    if USERS.get(user_id) is None:
        USERS.update({user_id:User(user_id)})
    if USERS[user_id].WHERE_I_WAS == '':
        USERS[user_id].WHERE_I_WAS = 'user_info'
        await get_name(message)
    elif USERS[user_id].WHERE_I_WAS == 'get_name':
        USERS[user_id].set_name(message.text)
        await get_surname(message)
    elif USERS[user_id].WHERE_I_WAS == 'get_surname':
        USERS[user_id].set_surname(message.text)
        await get_phone(message)
    elif USERS[user_id].WHERE_I_WAS == 'get_phone':
        USERS[user_id].set_phone(message.text)
        await get_email(message)
    elif USERS[user_id].WHERE_I_WAS == 'get_email':
        USERS[user_id].set_email(message.text)
        await get_birthday(message)
    elif USERS[user_id].WHERE_I_WAS == 'get_birthday':
        USERS[user_id].set_birthday(message.text)
        await get_sex(message)
    elif USERS[user_id].WHERE_I_WAS == 'get_sex':
        USERS[user_id].set_sex(message.text)
        USERS[user_id].WHERE_I_WAS =''
        await main_menu(message)

async def profile_print(message):
    user_id = message['from']['id']
    await bot.send_message(chat_id=user_id, text=USERS[user_id])

async def get_name(message):
    user_id = message['from']['id']
    USERS[user_id].WHERE_I_WAS = 'get_name'
    await bot.send_message(chat_id=user_id,text='Введите имя')

async def get_surname(message):
    user_id = message['from']['id']
    USERS[user_id].WHERE_I_WAS = 'get_surname'
    await bot.send_message(chat_id=user_id,text='Введите фамилию')


async def get_phone(message):
    user_id = message['from']['id']
    USERS[user_id].WHERE_I_WAS = 'get_phone'
    await bot.send_message(chat_id=user_id, text='Введите телефон')


async def get_email(message):
    user_id = message['from']['id']
    USERS[user_id].WHERE_I_WAS = 'get_email'
    await bot.send_message(chat_id=user_id, text='Введите e-mail')


async def get_birthday(message):
    user_id = message['from']['id']
    USERS[user_id].WHERE_I_WAS = 'get_birthday'
    await bot.send_message(chat_id=user_id, text='Введите день рождения')


async def get_sex(message):
    user_id = message['from']['id']
    USERS[user_id].WHERE_I_WAS = 'get_sex'
    await bot.send_message(chat_id=user_id, text='Введите пол')