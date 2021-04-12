import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from keyboards import menu
from loader import dp, db

token = ''


@dp.message_handler(Command('balance'))
async def show_menu(message: types.Message, state: FSMContext):
    user_data = db.select_user(id=message.from_user.id)
    global token
    token = {'Authorization': f'Bearer {user_data[3]}'}
    await state.set_state('NoBalanceData')


@dp.message_handler(state='NoBalanceData')
async def get_balance_data(message: types.Message, state: FSMContext):
    url = 'https://api.cloudvps.reg.ru/v1/balance_data'
    request = requests.get(url, headers=token)
    data = request.json()
    await message.answer(data)
    await state.finish()
