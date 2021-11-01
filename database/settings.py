DATABASE_CONFIG = {
    'connections': {
        # Dict format for connection
        # 'default': {
        #     'engine': 'tortoise.backends.asyncpg',
        #     'credentials': {
        #         'host': 'localhost',
        #         'port': '5432',
        #         'user': 'tortoise',
        #         'password': 'qwerty123',
        #         'database': 'test',
        #     }
        # },
        # 'default': 'postgres://postgres:qwerty123@localhost:5432/test',
        'default': 'sqlite://database.sqlite'
    },
    'apps': {
        'models': {
            'models': [
                'database.models.user'
            ]
        }
    },
    # 'routers': ['path.router1', 'path.router2'],
    'use_tz': False,
    'timezone': 'UTC'
}