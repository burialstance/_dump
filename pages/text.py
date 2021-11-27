from typing import Tuple, Optional

from aiogram.types import ParseMode

from database.schemas.profiles import Profile
from misc import icons, enum_to_icon
from misc.age import declination


def build_text_from_kwargs(header='Header', **body_parts) -> Tuple[str, str]:
    rows = [
        f'<b>{header}</b>',
        '\n'
    ]
    rows.extend([f"<code>{attr}</code>: {value}" for attr, value in body_parts.items()])

    text = '\n'.join(rows)
    parse_mode = ParseMode.HTML

    return text, parse_mode


def build_index_text():
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


def build_profile_text(form: Profile) -> Tuple[str, str]:
    country = f'{form.country.icon} {form.country.name}' if form.country else 'Неизвестно'
    gender = f'{enum_to_icon.icon_for_gender[form.gender]} {form.gender.value}' if form.gender else 'Неизвестно'
    age = f'{form.age} {declination(form.age)}' if form.age else 'Неизвестно'
    user_id = form.user_id
    rows = [
        f'Профиль пользователя',
        f'',
        f'{icons.person} <code>Пользователь:</code> {user_id}',
        f'{icons.underage} <code>Возраст:</code> {age}',
        f'{icons.world} <code>Страна:</code> {country}',
        f'{icons.couple} <code>Ваш пол:</code> {gender}'
    ]

    text = '\n'.join(rows)
    parse_mode = ParseMode.HTML
    return text, parse_mode