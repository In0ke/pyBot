import requests
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command('balance'))
async def show_menu(message: types.Message):
    user_token = db.get_user_token(id=message.from_user.id)
    token = {'Authorization': f'Bearer {user_token[0]}'}
    url = 'https://api.cloudvps.reg.ru/v1/balance_data'
    request = requests.get(url, headers=token)
    data = request.json()
    await message.answer(data)

