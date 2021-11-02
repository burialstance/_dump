from database.enums import GendersEnum, CountriesEnum
from misc import icons

icon_for_gender = {
    GendersEnum.MALE: icons.man,
    GendersEnum.FEMALE: icons.woman,
    GendersEnum.UNKNOWN: icons.eyes,
    GendersEnum.ANY: icons.couple
}

icon_for_country = {
    CountriesEnum.RUSSIA: icons.russia_flag,
    CountriesEnum.UKRAINE: icons.ukraine_flag,
    CountriesEnum.BELARUS: icons.belarus_flag,
    CountriesEnum.KAZAKHSTAN: icons.kazakhstan_flag,
    CountriesEnum.UZBEKISTAN: icons.uzbekistan_flag,
    CountriesEnum.TAJIKISTAN: icons.tajikistan_flag,
    CountriesEnum.TURKMENISTAN: icons.turkmenistan_flag,
    CountriesEnum.AZERBAIJAN: icons.azerbaijan_flag,
    CountriesEnum.ARMENIA: icons.armenia_flag,
    CountriesEnum.MOLDOVA: icons.moldova_flag,
    CountriesEnum.UNKNOWN: icons.world
}