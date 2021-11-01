from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

storage = MemoryStorage()
bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
