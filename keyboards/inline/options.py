from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button = InlineKeyboardMarkup(row_width=2)
confirmation_button = InlineKeyboardMarkup(row_width=2)


start_button = InlineKeyboardButton(text="Запустить сервер",
                                    callback_data='start')
button.insert(start_button)

stop_button = InlineKeyboardButton(text="Остановить серер",
                                   callback_data='stop')
button.insert(stop_button)

reboot_button = InlineKeyboardButton(text="Перезагрузить сервер",
                                     callback_data='reboot')
button.insert(reboot_button)

delete_button = InlineKeyboardButton(text="Удалить сервер",
                                     callback_data='delete')
button.insert(delete_button)

ok_button = InlineKeyboardButton(text="Поехали", callback_data="go")
confirmation_button.insert(ok_button)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
confirmation_button.insert(cancel_button)