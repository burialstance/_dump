from typing import Optional, Union

from pydantic import BaseModel
from aiogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply
)


class Page(BaseModel):
    text: Optional[str]
    parse_mode: Optional[str]
    reply_markup: Union[None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]

    class Config:
        arbitrary_types_allowed = True
