from loader import dp

from .userdata import UserMiddleware
from .throttling import ThrottlingMiddleware


if __name__ == 'middlewares':
    dp.middleware.setup(UserMiddleware())
    dp.middleware.setup(ThrottlingMiddleware())