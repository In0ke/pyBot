import requests
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command("os_list"))
async def get_os_list(message: types.Message):
    user_token = db.get_user_token(user_id=message.from_user.id)
    token = {"Authorization": f"Bearer {user_token[0]}"}
    url = "https://api.cloudvps.reg.ru/v1/images?type=distribution"
    request = requests.get(url, headers=token)
    data = request.json()
    os_list = []
    for i in range(0, len(data["images"])):
        os_list.append(data["images"][i]["slug"])
    await message.answer(text=str(os_list))
