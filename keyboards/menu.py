from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Старт'),
            KeyboardButton(text='Стоп'),
        ],
        [
            KeyboardButton(text='Перезагрузка')
        ],
        [
            KeyboardButton(text='Удалить')
        ],
    ],
    resize_keyboard=True
)