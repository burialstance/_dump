from database.exceptions.base import BaseDatabaseException


class ProfileBaseException(BaseDatabaseException):
    ...


class ProfileDoesNotExist(ProfileBaseException):
    ...

class ProfileAgeException(ProfileBaseException):
    ...


