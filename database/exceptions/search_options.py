from database.exceptions.base import BaseDatabaseException


class SearchOptionsBaseException(BaseDatabaseException):
    ...


class SearchOptionsDoesNotExist(SearchOptionsBaseException):
    ...


class SearchOptionsAgeException(SearchOptionsBaseException):
    ...


class FromAgeGreaterThanToAge(SearchOptionsAgeException):
    ...


class ToAgeLessThanFromAge(SearchOptionsAgeException):
    ...