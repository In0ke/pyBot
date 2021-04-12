from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback

button = InlineKeyboardMarkup(row_width=2)

start_button = InlineKeyboardButton(text="Запустить сервер",
                                    callback_data=buy_callback.new(item_name='start'))
button.insert(start_button)

stop_button = InlineKeyboardButton(text="Остановить серер",
                                   callback_data=buy_callback.new(item_name='stop'))
button.insert(stop_button)

reboot_button = InlineKeyboardButton(text="Перезагрузить сервер",
                                     callback_data=buy_callback.new(item_name='reboot'))
button.insert(reboot_button)

delete_button = InlineKeyboardButton(text="Удалить сервер",
                                     callback_data=buy_callback.new(item_name='delete'))
button.insert(delete_button)

# cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
# button.insert(cancel_button)


apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url="https://freshmart.com.ua/product/yabloko-gala-116.html")
    ]
])