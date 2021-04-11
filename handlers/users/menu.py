from aiogram import types
from aiogram.dispatcher.filters import Command, Text

from keyboards import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer("Выберите действие", reply_markup=menu)


@dp.message_handler(text="Старт")
async def start_server(message: types.Message):
    await message.answer('Вы запустили сервер.')


@dp.message_handler(Text('Стоп'))
async def stop_server(message: types.Message):
    await message.answer('Вы остановили сервер')
