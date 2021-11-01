from aiogram import types, Dispatcher

from misc import commands


async def set_default_commands(dispatcher: Dispatcher):
    await dispatcher.bot.set_my_commands([
        types.BotCommand(command, description)
        for command, description in commands.BOT_COMMANDS.items()
    ])