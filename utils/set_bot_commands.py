from aiogram import types, Dispatcher

from misc.bot_commands import BOT_COMMANDS


async def set_default_commands(dispatcher: Dispatcher):
    await dispatcher.bot.set_my_commands([
        types.BotCommand(command, description)
        for command, description in BOT_COMMANDS.items()
    ])