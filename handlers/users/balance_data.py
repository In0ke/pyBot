import requests
from aiogram import types
from aiogram.dispatcher.filters import Command

from api.regru_cloud import cloud_api
from entities.user import User
from loader import dp
from templates.render_templates import render_template


@dp.message_handler(Command("balance"))
async def get_balance_data(message: types.Message):
    template_name = "get_balance"
    user = User(message.from_user.id)
    balance_data = cloud_api.get_balance_data(user)
    massage_txt = render_template(template_name, **balance_data.dict())
    await message.answer(massage_txt)
