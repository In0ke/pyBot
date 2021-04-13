from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.options import confirmation_button
from loader import dp


@dp.message_handler(Command('new_server'))
async def create_server(message: types.Message, state: FSMContext):
    await message.answer(
        'Давай создадим новый сервер \n'
        'У нас будет 4 шага: \n'
        '1. Выберем между чистой ОС или готовым приложением. \n'
        '2. Выберем необходимую операционную систему или приложение. \n'
        '3. Выберем тариф. \n'
        '4. Ждем пока сервер создастся',
        reply_markup=confirmation_button
    )
    # await state.set_state('not_selected_image_type')


@dp.message_handler(state='not_selected_image_type')
async def select_image_type(message: Union[types.Message, types.CallbackQuery], state: FSMContext):
    await message.answer(text='not_selected_image_type')
    await state.set_state('not_selected_image')


@dp.message_handler(state='not_selected_image')
async def select_image(message: types.Message, state: FSMContext):
    await message.answer(text='not_selected_image')
    await state.set_state('not_selected_plan')


@dp.message_handler(state='not_selected_plan')
async def select_plan(message: types.Message, state: FSMContext):
    await message.answer(text='not_selected_plan')
    await state.set_state('create_server')


@dp.message_handler(state='create_server')
async def create_server(message: types.Message, state: FSMContext):
    await message.answer(text='create_server')
    await state.finish()


@dp.callback_query_handler(text="go")
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Поехали")
    await state.set_state('not_selected_image_type')


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.answer("Отменяем заказ", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()
