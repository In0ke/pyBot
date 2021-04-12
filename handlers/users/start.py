import sqlite3
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.support import help_token_url
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)

    await message.answer(
        f'Привет! {message.from_user.full_name}! \n '
        'Добро пожаловать в Cloud VPS бота. \n'
        'Я помогу облегчить твою работу с Облачными серверами Reg.ru. \n\n'
        'Для начала, давай получим доступ к твоему окружению. \n'
        'Отправь мне свой API-Ключ',
        reply_markup=help_token_url)

    await state.set_state('NoToken')


@dp.message_handler(state='NoToken')
async def enter_token(message: types.Message, state: FSMContext):
    try:
        db.update_user_token(id=message.from_user.id, token=message.text)
    except sqlite3.IntegrityError as err:
        print(err)

    await message.answer('Отлично! Мы добавили API ключ. \n'
                         f'Можем приступать к работе.')
    await state.finish()
