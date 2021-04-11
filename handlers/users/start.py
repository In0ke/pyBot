import re

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link

from filters import IsPrivate
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')

# @dp.message_handler(CommandStart(deep_link=re.compile(r"\d\d\d")), IsPrivate())
# async def bot_start(message: types.Message):
#     deep_link_args = message.get_args()
#     await message.answer(f"Привет, {message.from_user.full_name}!\n"
#                          f"Вы находитесь в личной переписке \n"
#                          f"В вышей команде есть диплинк \n"
#                          f"Вы передали аргумент {deep_link_args}")
#
#
# @dp.message_handler(CommandStart(), IsPrivate())
# async def bot_start(message: types.Message):
#     deep_link = await get_start_link(payload="123")
#     await message.answer(f"Привет, {message.from_user.full_name}!\n"
#                          f"Вы находитесь в личной переписке \n"
#                          f"В вышей команде нет диплинк \n"
#                          f"Ваша диплинк ссылка - {deep_link}")
