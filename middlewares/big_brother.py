import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import banned_users


class BigBrother(BaseMiddleware):
    # 1
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info("-----------------------Новый апдейт!-----------------------")
        logging.info("1. Pre Process Update")
        logging.info("Следующая точка: Process Update")
        data["middleware_data"] = "Это пройдет до on_post_process_update"
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return

        if user is banned_users:
            raise CancelHandler()

    # 2
    async def on_process_update(self, update: types.Update, data: dict):
        logging.info(f"2. Process Update, {data}")
        logging.info("Следующая точка: Pre Process Message")

    # 3
    async def on_pre_process_message(self, message: types.Message, data: dict):
        logging.info(f"3. Pre Process Message, {data=}")
        logging.info("Следующая точка: Filters, Process Message")
        data["middleware_data"] = "Это пройдет в on_process_message"

