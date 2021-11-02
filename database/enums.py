from enum import Enum


class GendersEnum(str, Enum):
    UNKNOWN = 'неизвестный'
    ANY = 'любой'

    MALE = 'мужской'
    FEMALE = 'женский'


class CountriesEnum(str, Enum):
    UNKNOWN = 'неизвестная'
    ANY = 'любая'

    RUSSIA = 'Россия'
    UKRAINE = 'Украина'
    BELARUS = 'Беларусь'
    KAZAKHSTAN = 'Казахстан'
    UZBEKISTAN = 'Узбекистан'
    TAJIKISTAN = 'Таджикистан'
    TURKMENISTAN = 'Туркменистан'
    AZERBAIJAN = 'Азербайджан'
    ARMENIA = 'Армения'
    MOLDOVA = 'Молдова'
