from config import *

async def main_menu(message):
    user_id = message['from']['id']
    kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    reg_btn = types.KeyboardButton(text='Регистрация')
    profile_btn = types.KeyboardButton(text='Профиль')
    kbrd.add(reg_btn,profile_btn)
    await bot.send_message(user_id,text='Сделайте ваш выбор',reply_markup=kbrd)