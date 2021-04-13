from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.db_api import add_to_database
from utils.db_api.database import create_db
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)
    # try:
    #     db.create_table_users()
    # except Exception as e:
    #     print(e)
    # print(db.select_all_user())
    await create_db()
    # await add_to_database.add_item()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
