from typing import Union

from aiogram import types
# from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from keyboards.inline.create_server_keyboards import categories_keyboard
from keyboards.inline.options import confirmation_button
from loader import dp


@dp.message_handler(Command('new_server'))
async def show_alert(message: types.Message):
    await message.answer(
        'Давай создадим новый сервер \n'
        'У нас будет 4 шага: \n'
        '1. Выберем между чистой ОС или готовым приложением. \n'
        '2. Выберем необходимую операционную систему или приложение. \n'
        '3. Выберем тариф. \n'
        '4. Ждем пока сервер создастся',
        await list_categories(message)
    )
    # await state.set_state('not_selected_image_type')


# Та самая функция, которая отдает категории. Она может принимать как CallbackQuery, так и Message
# Помимо этого, мы в нее можем отправить и другие параметры - category, subcategory, item_id,
# Поэтому ловим все остальное в **kwargs
async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    # Клавиатуру формируем с помощью следующей функции (где делается запрос в базу данных)
    markup = await categories_keyboard()

    # Проверяем, что за тип апдейта. Если Message - отправляем новое сообщение
    if isinstance(message, Message):
        await message.answer("Смотри, что у нас есть", reply_markup=markup)

    # Если CallbackQuery - изменяем это сообщение
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)

