from database.exceptions.base import BaseDatabaseException

class UserBaseException(BaseDatabaseException):
    ...

class UserDoesNotExist(UserBaseException):
    ...