from typing import Tuple, Optional

from aiogram.types import ParseMode

from database.models.profiles import Profile
from database.models.search_options import SearchOptions
from misc import icons, enum_to_icon
from misc.age import declination, declination_from


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


def build_profile_text(profile: Profile) -> Tuple[str, str]:
    country = f'{profile.country.icon} {profile.country.name}' if profile.country else 'Неизвестно'
    gender = f'{enum_to_icon.icon_for_gender[profile.gender]} {profile.gender}' if profile.gender else 'Неизвестно'
    age = f'{profile.age} {declination(profile.age)}' if profile.age else 'Неизвестно'
    user_id = profile.user_id

    rows = [
        f'{icons.person} Профиль пользователя',
        f'',
        f'<code>Идентификатор:</code> {user_id}',
        f'{icons.underage} <code>Возраст:</code> {age}',
        f'{icons.world} <code>Страна:</code> {country}',
        f'{icons.couple} <code>Ваш пол:</code> {gender}'
    ]

    text = '\n'.join(rows)
    parse_mode = ParseMode.HTML
    return text, parse_mode


def build_search_options_text(s_options: SearchOptions):
    age_from = f'от {s_options.from_age} {declination_from(s_options.from_age)}' if s_options.from_age else None
    age_to = f'до {s_options.to_age} {declination_from(s_options.to_age)}' if s_options.to_age else None
    age = ' '.join(list(filter(None, [age_from, age_to]))) if age_from or age_to else 'Без ограничений'
    country = f'{s_options.country.icon} {s_options.country.name}' if s_options.country else 'Все'
    gender = f'{enum_to_icon.icon_for_gender.get(s_options.gender)} {s_options.gender}' if s_options.gender else 'Любой'

    rows = [
        f'{icons.gear} Поисковые настройки',
        '',
        f'{icons.underage} <code>Возраст:</code> {age}',
        f'{icons.world} <code>Страна:</code> {country}',
        f'{icons.couple} <code>Пол:</code> {gender}'
    ]

    text = '\n'.join(rows)
    parse_mode = ParseMode.HTML
    return text, parse_mode