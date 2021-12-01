from database.exceptions.base import BaseDatabaseException


class BaseCountryException(BaseDatabaseException):
    ...


class CountryDoesNotExist(BaseCountryException):
    ...