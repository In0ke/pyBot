from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loader import db

steps_data = CallbackData("show_menu", "level", "select_os_app", "select_tarif", )


def make_callback_data(level, select_os_app="0", select_tarif="0"):
    return steps_data.new(level=level, select_os_app=select_os_app, select_tarif=select_tarif)


async def categories_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup()
    os_list = db.select_all_os()
    for os in os_list:
        button_text = f"{os.name}"

        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, select_os_app=os.slug)

        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    return markup
