class InvalidCommandError(Exception):
    def __init__(self, message = "Informe um comando válido. Use help para ver a lista de comandos."):
        super().__init__(message)