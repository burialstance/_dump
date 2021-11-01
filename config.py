import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Loading token from .env
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_ADMINS = list(map(int, os.getenv('TELEGRAM_ADMINS').split(',') if os.getenv('TELEGRAM_ADMINS') else []))
