from pathlib import Path
from colorama import Fore as fg
import os, getpass


# Nome de usuário da máquina
USERNAME = getpass.getuser()

# Caminho absoluto da ferramenta, 'fora do src'
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Caminho dos logs
LOG_DIR = BASE_DIR / 'logs'


class Colors:
    """Esquema de cores"""

    # cores de alerta
    SUCCESS = fg.GREEN
    ERROR = fg.RED
    INFO = fg.BLUE
    WARNING = fg.YELLOW

    # cores de texto
    TEXT = fg.WHITE
    TITLE = fg.GREEN

    # cores da ferramenta
    ONE = fg.GREEN
    TWO = fg.WHITE
