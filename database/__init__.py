from tortoise import Tortoise
from loguru import logger

from . import settings


async def database_init():
    await Tortoise.init(settings.DATABASE_CONFIG)
    await Tortoise.generate_schemas()
    logger.info("Tortoise inited!")


async def database_close():
    await Tortoise.close_connections()
    logger.info("Tortoise closed!")


