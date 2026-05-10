from pathlib import Path
from colorama import Fore as fg


# Caminho absoluto da tool
BASE_DIR = Path(__file__).resolve().parent.parent

# FFMPEG Paths
FFMPEG_PATH = BASE_DIR / 'bin/ffmpeg/ffmpeg.exe'
FFPLAY_PATH = BASE_DIR / 'bin/ffmpeg/ffplay.exe'
FFPROBE_PATH = BASE_DIR / 'bin/ffmpeg/ffprobe.exe'


class Colors:
    # tool
    PRIMARY = fg.RED
    SECONDARY = fg.WHITE

    # texts
    TEXT = fg.WHITE
    TITLE = fg.RED

    # alerts
    SUCCESS = fg.GREEN
    ERROR = fg.RED
    INFO = fg.BLUE
    WARNING = fg.YELLOW


# Dicionario do response
RESPONSE_DICT = {
    'success': Colors.SUCCESS,
    'error': Colors.ERROR,
    'info': Colors.INFO,
    'warning': Colors.WARNING
}



