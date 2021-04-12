import requests
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.options import button
from loader import dp, db


@dp.message_handler(Command('server_list'))
async def get_server_list(message: types.Message):
    user_token = db.get_user_token(id=message.from_user.id)
    token = {'Authorization': f'Bearer {user_token[0]}'}
    url = 'https://api.cloudvps.reg.ru/v1/reglets'
    request = requests.get(url, headers=token)
    response = request.json()
    for value in response["reglets"]:
        text = str((value["name"], value["id"], value["ip"], value["image"]["name"], value['status']))
        await message.answer(text=str(text), reply_markup=button)

#
# @dp.callback_query_handler(text_contains="start")
# async def buying_pear(call: CallbackQuery, reglet_id: str):
#     await call.answer(cache_time=60)
#     pass
#
#
# @dp.callback_query_handler(text_contains="stop")
# async def buying_pear(call: CallbackQuery, reglet_id: str):
#     await call.answer(cache_time=60)
#     pass
#
#
# @dp.callback_query_handler(text_contains="reboot")
# async def buying_pear(call: CallbackQuery, reglet_id: str):
#     await call.answer(cache_time=60)
#     pass
#
#
# @dp.callback_query_handler(text_contains="delete")
# async def buying_pear(call: CallbackQuery, reglet_id: str):
#     await call.answer(cache_time=60)
#     pass
