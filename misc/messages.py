from typing import Tuple

from aiogram import types
from aiogram.types import ParseMode


def build_text_from_kwargs(header='Header', **body_parts) -> Tuple[str, str]:
    rows = [
        f'<b>{header}</b>',
        '\n'
    ]
    rows.extend([f"<code>{attr}</code>: {value}" for attr, value in body_parts.items()])

    text = '\n'.join(rows)
    parse_mode = ParseMode.HTML

    return text, parse_mode


def build_index_page_text():
    rows = [
        '<b>Анонимный чат</b>'
    ]

    text = '\n'.join(rows)
    parse_mode = ParseMode.HTML
    return text, parse_mode


def build_rules_text():
    rows = [
        'Будьте вежливы со всеми участниками чата.',
        'Не публикуйте сообщение, если оно может обидеть или оскорбить других людей.',
        'Берегите время других участников.',
        'Следите, чтобы сообщение не было аморальным, неприличным.',
        'Не публикуйте фотографии других людей и сведения о них без их согласия. Это запрещено законом.',
        'Сохраняйте спокойствие в конфликтной ситуации.',
        'При первых признаках конфликта немедленно прекращайте свое участие в обсуждении.',
        'Соблюдайте закон. Не делайте репост запрещенной информации, например, экстремистской.'
    ]

    text = '\n'.join(rows)
    parse_mode = None
    return text, parse_mode


