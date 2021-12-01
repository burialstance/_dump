import os

from aiogram import types

from conf.settings import settings


def fetch_database_models():
    models_path = settings.BASE_DIR.joinpath(os.path.join('database', 'models'))
    models_in_dir = [
        i for i in models_path.iterdir() if all([
            i.is_file(),
            i.suffix == '.py',
            not '__' in i.name
        ])
    ]

    return [f'database.models.{model_name.name.removesuffix(model_name.suffix)}' for model_name in models_in_dir]


async def notify_telegram_about_exception(update: types.Update, message: str):
    handled = False

    if update.callback_query is not None:
        await update.callback_query.answer(message, show_alert=True)
        handled = True
    elif update.message is not None:
        chat_id = update.message.chat.id
        await update.bot.send_message(chat_id, message)
        handled = True

    return handled


