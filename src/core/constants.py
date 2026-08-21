from pathlib import Path
from colorama import Fore as fg
import os, getpass


# -------- USUÁRIO E SISTEMA -------- #

# Nome de usuário da máquina
USERNAME = getpass.getuser()


# -------- CAMINHOS -------- #

# Caminho absoluto da ferramenta, 'fora do src'
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Caminho dos logs
LOG_DIR = BASE_DIR / 'logs'

# Caminho dos .jsom
JSON_DIR = BASE_DIR / 'json' 

# Caminho FFMPEG
FFMPEG_DIR = BASE_DIR / 'bin' / 'ffmpeg'

# Caminho para saidas
OUTPUT_DIR = BASE_DIR / 'bin' / 'output'


# -------- ATALHOS -------- #
# apenas o nome dos arquivos, não o caminho
# as funções que tratam json já buscam por padrão o dir 'json'

SHORTS_JSON = 'shorts.json'


# -------- ASSETS --------#

MONITOR_HTML = BASE_DIR / 'src' / 'ui' / 'assets' / 'monitor.html'


# -------- CORES -------- #

class Colors:
    """Esquema de cores"""

    # cores de alerta
    SUCCESS = fg.GREEN
    ERROR = fg.RED
    INFO = fg.BLUE
    WARNING = fg.YELLOW

    # cores de texto
    TEXT = fg.LIGHTWHITE_EX
    TITLE = fg.RED

    # cores da ferramenta
    ONE = fg.RED
    TWO = fg.LIGHTWHITE_EX
