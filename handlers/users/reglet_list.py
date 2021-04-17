from aiogram import types
from aiogram.dispatcher.filters import Command
from loguru import logger

from api.regru_cloud import cloud_api
from entities.user import User
from keyboards.inline.options import button
from loader import dp
from templates.render_templates import render_template


@dp.message_handler(Command("server_list"))
async def get_server_list(message: types.Message):
    template_name = "get_reglet_list"
    user = User(message.from_user.id)
    server_data = cloud_api.get_server_list(user)
    for reglet in server_data.reglets:
        massage_txt = render_template(template_name, **reglet.dict())
        logger.info(f"Send message for user {user.user_id} with message {massage_txt}")
        await message.answer(massage_txt, reply_markup=button)
