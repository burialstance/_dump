from typing import Type, List
from tortoise.signals import pre_save, post_save
from loguru import logger

from database.models.user import User
from database.models.search_options import SearchOptions


@pre_save(User)
async def signal_create_search_options_for_user(sender: "Type[User]", instance: User, using_db, update_fields) -> None:
    logger.debug(f'pre_save {instance} signal update_fields: {update_fields}')


@post_save(User)
async def signal_create_search_options(sender: "Type[User]", instance: User, created: bool,
                                       using_db: "Optional[BaseDBAsyncClient]",
                                       update_fields: List[str]) -> None:
    if created:
        logger.debug(f'post_save {instance} signal update_fields: {update_fields}')