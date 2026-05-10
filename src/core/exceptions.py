

class PathNotFoundError(Exception):
    """Erro de path não encontrado"""

    def __init__(self, path):
        self.path = path
        super().__init__(f'Caminho não encontrado: {self.path}')

