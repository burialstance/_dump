from aiogram.types import ParseMode
from aiogram.utils.markdown import text, bold, code

from loguru import logger
from aiogram import Dispatcher

from config import TELEGRAM_ADMINS


async def notify_admins(dispatcher: Dispatcher, message: str, header='NOTIFY SYSTEM'):
    notify = '\n'.join([
        text(code(header)),
        text(bold(message))
    ])

    for admin_id in TELEGRAM_ADMINS:
        try:
            await dispatcher.bot.send_message(admin_id, notify, parse_mode=ParseMode.MARKDOWN)
        except Exception as err:
            logger.exception(err)