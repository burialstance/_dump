from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from schemas.page import Page


async def build_referrals_page():
    text, parse_mode = ..., ...
    reply_markup = ...
    return Page(text=text, parse_mode=parse_mode, reply_markup=reply_markup)


@dp.message_handler(Command('referrals'))
async def process_referrals_cmd(m: types.Message):
    page = await build_referrals_page()
    return await m.answer(**page.dict(exclude_unset=True))