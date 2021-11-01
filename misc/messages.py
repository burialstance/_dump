from typing import Tuple

from aiogram import types
from aiogram.types import ParseMode


async def build_start_message(**body_parts) -> Tuple[str, str]:
    rows = [
        '<b>process start command</b>',
        '\n'
    ]
    rows.extend([f"<code>{attr}</code>: {value}" for attr, value in body_parts.items()])

    text = '\n'.join(rows)
    parse_mode = ParseMode.HTML

    return text, parse_mode
