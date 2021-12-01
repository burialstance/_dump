class BaseDatabaseException(Exception):
    def __init__(self, telegram_notify: str = ''):
        self.telegram_notify = telegram_notify

