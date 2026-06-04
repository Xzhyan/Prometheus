import pathlib
from pathlib import Path

# core/exceptions
from .exceptions import PathNotFoundError, FilePathNotFoundError



def path_check(path):
    path = Path(path)

    if not path.exists():
        raise PathNotFoundError(f"{path}: caminho não encontrado.")
    
    else:
        True


def file_check(file_path):
    file_path = Path(file_path)

    if not file_path.is_file():
        raise FilePathNotFoundError(f"{file_path}: arquivo não encontrado.")
    
    else:
        return True
