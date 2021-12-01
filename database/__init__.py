from tortoise import Tortoise
from loguru import logger

from database import logging
from database.settings import DATABASE_CONFIG
from database.models.countries import Country


async def create_tables():
    await Country.create_countries()


async def database_init():
    await Tortoise.init(DATABASE_CONFIG)
    await Tortoise.generate_schemas()
    await create_tables()
    logger.info("Tortoise inited!")


async def database_close():
    await Tortoise.close_connections()
    logger.info("Tortoise closed!")
