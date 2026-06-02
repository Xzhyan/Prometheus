from pathlib import Path
from colorama import Fore as fg


# caminho absoluto da ferramenta, 'fora do src'
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Colors:
    """Esquema de cores"""

    # cores de alerta
    SUCCESS = fg.GREEN
    ERROR = fg.RED
    INFO = fg.BLUE
    WARNING = fg.YELLOW

    # cores de texto
    TEXT = fg.WHITE
    TITLE = fg.RED

    # cores da ferramenta
    ONE = fg.RED
    TWO = fg.WHITE



