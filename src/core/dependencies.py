import pathlib, time
from pathlib import Path

# constants/paths
from .constants import LOG_DIR, JSON_DIR, FFMPEG_DIR, OUTPUT_DIR

# core/exceptions
from .exceptions import PathNotFoundError, FilePathNotFoundError

# ui
from ui.ui_console import alert


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


def check_all():
    """Verifica todas as dependencias da ferramenta"""
    
    alert('info', "Verificando as dependências da ferramenta")

    path_list = [LOG_DIR, JSON_DIR, FFMPEG_DIR, OUTPUT_DIR]

    try:
        for path in path_list:
            path.mkdir(exist_ok=True)

            time.sleep(0.5)
            alert('success', f"{path}: ok")
        
        alert('info', "Tudo pronto, aguarde alguns segundos...")
        time.sleep(3)
        return True

    except Exception as e:
        alert('error', str(e))
