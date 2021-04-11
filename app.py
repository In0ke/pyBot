from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from loader import db


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)
    try:
        db.create_table_users()
    except Exception as e:
        print(e)
    db.delete_users()
    print(db.select_all_user())


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
