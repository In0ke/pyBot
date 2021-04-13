from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


# @dp.message_handler(Command('menu'))
# async def show_menu(message: types.Message):
#     await list_categorises(message)

# async def list_categorises(message: Union[types.Message, types.CallbackQuery], **kwargs):
#     markup = await categotis_keyboard()
