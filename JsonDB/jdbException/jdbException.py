class NewDatabaseError(Exception):
    pass


class JdbFileNotFoundError(Exception):
    pass


class TableNotFoundError(Exception):
    pass


class TableAlreadyExistsError(Exception):
    pass


class ValueNotUniqueError(Exception):
    pass


class ValueNotFoundError(Exception):
    pass


class  KeyNotFoundError(Exception):
    pass