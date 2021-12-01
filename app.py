import logging

from loguru import logger
from aiogram import Dispatcher, executor
import filters
import middlewares
import handlers
from loader import dp
from database import database_init, database_close
from utils.set_bot_commands import set_bot_commands
from utils.notify_admins import notify_admins


logging.basicConfig(level=logging.DEBUG)


async def on_startup(dispatcher: Dispatcher):
    logger.info("on_startup...")
    await database_init()
    await set_bot_commands(dp=dispatcher)
    await notify_admins(dp=dispatcher, text='Startup')


async def on_shutdown(dispatcher: Dispatcher):
    logger.info("on_shutdown...")
    await database_close()


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp, skip_updates=True,
        on_startup=on_startup, on_shutdown=on_shutdown
    )
