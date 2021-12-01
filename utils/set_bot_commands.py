from typing import Dict

from aiogram import types, Dispatcher

from misc import icons

BOT_COMMANDS = {
    "search": f"{icons.search} Поиск собеседника",
    "next": f"{icons.arrow_right} Переключить собеседника",
    "stop": f"{icons.stop} Остановить диалог",
    "search_options": f"{icons.gear} Параметры поиска",
    "referrals": f"{icons.persons} Мои рефералы",
    "profile": f"{icons.person} Мой профиль"
}


async def set_bot_commands(dp: Dispatcher, commands: Dict[str, str] = None):
    commands = commands or BOT_COMMANDS

    await dp.bot.set_my_commands([
        types.BotCommand(command, description)
        for command, description in commands.items()
    ])
