from aiogram.types import ParseMode
from aiogram.utils.markdown import text, bold, code

from loguru import logger
from aiogram import Bot

from conf.settings import settings


async def notify(chat_id: int, text: str, bot: Bot, header: str = 'NOTIFY SYSTEM'):
    message = '\n'.join([code(header), bold(text)])
    try:
        await bot.send_message(chat_id, message, parse_mode=ParseMode.MARKDOWN)
    except Exception as err:
        logger.exception(err)


async def notify_admins(bot: Bot, text: str):
    for admin_id in settings.TELEGRAM_ADMINS:
        await notify(chat_id=admin_id, text=text, bot=bot)
