
class InvalidCommandError(Exception):
    def __init__(
            self,
            message="Informe um comando válido."
    ):
        super().__init__(message)


class CommandNotFoundError(Exception):
    def __init__(
            self,
            message="Comando não encontrado."
    ):
        super().__init__(message)


class FilePathNotFoundError(Exception):
    pass


class PathNotFoundError(Exception):
    pass


class ShortNotFoundError(Exception):
    pass
