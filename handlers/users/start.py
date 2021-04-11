import re
import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link

from filters import IsPrivate
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)

    count_users = db.count_users()[0]
    await message.answer(
        "\n".join([
            f'Привет! {message.from_user.full_name}!',
            'Ты был занесен в базу'
            f'В базе <b>{count_users}</b> пользователей'
        ])
    )



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
