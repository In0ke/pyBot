from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loader import db

steps_data = CallbackData("show_menu", "level", "select_os_app", "select_tarif", )


def make_callback_data(level, select_os_or_app="0", select_os_app="0", select_tarif="0"):
    return steps_data.new(level=level, select_os_or_app=select_os_or_app, select_os_app=select_os_app,
                          select_tarif=select_tarif)


async def select_tarif_line_keyboard():
    markup = InlineKeyboardMarkup()
    markup.insert(
        InlineKeyboardButton(text='Старт', callback_data='start')
    )
    markup.insert(
        InlineKeyboardButton(text='Стандарт', callback_data='standard')
    )
    markup.insert(
        InlineKeyboardButton(text='Высокочастотные', callback_data='turbo')
    )
    markup.insert(
        InlineKeyboardButton(text='Выделенные', callback_data='dedicated')
    )

    return markup


async def select_os_or_app_keyboard():
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()
    markup.insert(
        InlineKeyboardButton(text='Чистая ОС', callback_data='os')
    )
    markup.insert(
        InlineKeyboardButton(text='Готовое приложение', callback_data='apps')
    )

    return markup


async def categories_keyboard():
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup()
    os_list = db.select_all_os()
    for os in os_list:
        button_text = f"{os[0]}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, select_os_app=os[2])

        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    return markup


async def tarif_keyboard():
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    tarif_list = db.select_tarif('standard')
    for tarif in tarif_list:
        button_text = f"{tarif}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, select_os_app=tarif)

        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    return markup
