import logging
import asyncio

from loguru import logger
from aiogram import Dispatcher, executor

import middlewares, filters, handlers
from loader import dp
from database import database_init, database_close
from utils.set_bot_commands import set_default_commands
from utils.notify_admins import notify_admins


logging.basicConfig(level=logging.DEBUG)


async def on_startup(dispatcher: Dispatcher):
    logger.info("on_startup...")
    await set_default_commands(dispatcher=dispatcher)
    await notify_admins(dispatcher=dispatcher, message='Startup')


async def on_shutdown(dispatcher: Dispatcher):
    logger.info("on_shutdown...")
    await database_close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(database_init())
    executor.start_polling(
        loop=loop, dispatcher=dp,
        on_startup=on_startup, on_shutdown=on_shutdown,
        skip_updates=True
    )
