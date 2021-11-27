from typing import Type, List
from tortoise.signals import pre_save, post_save
from loguru import logger

from .models.users import User
from .models.profiles import Profile
from .models.search_options import SearchOptions


@post_save(User)
async def signal_create_default_profile(
        sender: "Type[User]", instance: User, created: bool,
        using_db: "Optional[BaseDBAsyncClient]",
        update_fields: List[str]) -> None:
    if created:
        await Profile.create(user=instance)


@post_save(User)
async def signal_create_default_search_options(
        sender: "Type[User]", instance: User, created: bool,
        using_db: "Optional[BaseDBAsyncClient]",
        update_fields: List[str]) -> None:
    if created:
        await SearchOptions.create(user=instance)