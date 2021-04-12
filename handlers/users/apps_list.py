import requests
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command('apps_list'))
async def get_apps_list(message: types.Message):
    user_token = db.get_user_token(id=message.from_user.id)
    token = {'Authorization': f'Bearer {user_token[0]}'}
    url = 'https://api.cloudvps.reg.ru/v1/images?type=application'
    request = requests.get(url, headers=token)
    data = request.json()
    apps_list = []
    for i in range(0, len(data['images'])):
        apps_list.append(data['images'][i]['name'])
    await message.answer(text=str(apps_list))