from aiogram import types
from aiogram.utils.callback_data import CallbackData


on_age_clicked = CallbackData('settings_age_clicked')
on_age_setup_clicked = CallbackData('age_setup', 'from_age', 'to_age')
on_age_setup_back = CallbackData('age_setup_back')

on_country_clicked = CallbackData('settings_country_clicked')
on_country_setup_clicked = CallbackData('country_setup', 'country')
on_country_setup_back = CallbackData('country_setup_back')

settings_kb = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        types.InlineKeyboardButton('🔞 Возраст', callback_data=on_age_clicked.new()),
        types.InlineKeyboardButton('🌎 Страна', callback_data=on_country_clicked.new())
    ]
])

setup_age_kb = types.InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        types.InlineKeyboardButton('до 12 лет', callback_data=on_age_setup_clicked.new(from_age=0, to_age=12)),
        types.InlineKeyboardButton('13-15 лет', callback_data=on_age_setup_clicked.new(from_age=13, to_age=15))
    ],
    [
        types.InlineKeyboardButton('16-18 лет', callback_data=on_age_setup_clicked.new(from_age=16, to_age=18)),
        types.InlineKeyboardButton('19-23 лет', callback_data=on_age_setup_clicked.new(from_age=19, to_age=23))
    ],
    [
        types.InlineKeyboardButton('24-27 лет', callback_data=on_age_setup_clicked.new(from_age=24, to_age=27)),
        types.InlineKeyboardButton('28-30+ лет', callback_data=on_age_setup_clicked.new(from_age=28, to_age=100)),
    ],
    [
        types.InlineKeyboardButton('◀️ Назад', callback_data=on_age_setup_back.new())
    ]
])

setup_country_kb = types.InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [
        types.InlineKeyboardButton(text='🇷🇺 Россия', callback_data=on_country_setup_clicked.new(country='Россия')),
        types.InlineKeyboardButton(text='🇺🇦 Украина', callback_data=on_country_setup_clicked.new(country='Украина')),
    ],
    [
        types.InlineKeyboardButton(text='🇧🇾 Беларусь',
                                   callback_data=on_country_setup_clicked.new(country='Беларусь')),
        types.InlineKeyboardButton(text='🇰🇿 Казахстан',
                                   callback_data=on_country_setup_clicked.new(country='Казахстан')),
    ],
    [
        types.InlineKeyboardButton(text='🇺🇿 Узбекистан',
                                   callback_data=on_country_setup_clicked.new(country='Узбекистан')),
        types.InlineKeyboardButton(text='🇹🇯 Таджикистан',
                                   callback_data=on_country_setup_clicked.new(country='Таджикистан')),
    ],
    [
        types.InlineKeyboardButton(text='🇹🇲 Туркменистан',
                                   callback_data=on_country_setup_clicked.new(country='Туркменистан')),
        types.InlineKeyboardButton(text='🇦🇿 Азербайджан',
                                   callback_data=on_country_setup_clicked.new(country='Азербайджан')),
    ],
    [
        types.InlineKeyboardButton(text='🇦🇲 Армения',
                                   callback_data=on_country_setup_clicked.new(country='Армения')),
        types.InlineKeyboardButton(text='🇲🇩 Молдова',
                                   callback_data=on_country_setup_clicked.new(country='Молдова')),
    ],
    [
        types.InlineKeyboardButton(text='◀️ Назад', callback_data=on_country_setup_back.new())
    ]
])
