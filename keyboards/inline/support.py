from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback


help_token_url = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Узнать, как получить ключ", url="https://www.reg.ru/support/vps-servery/oblachnie-serveri-vps/rabota-s-serverom/kak-poluchit-ili-smenit-kluch-api")
    ]
])