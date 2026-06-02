import subprocess, platform, sys

# core
from core.constants import Colors
from core.exceptions import InvalidCommandError

# ui
from ui.ui_console import alert


def shutdown():
    """Finalizar a ferramenta"""

    alert('info', "Finalizando...")
    sys.exit(0)


def clear():
    """Limpa a tela da ferramenta"""

    cmd = 'cls' if platform.system() == 'Windows' else 'clear'
    subprocess.run(cmd, shell=True)


def entry():
    """Recebe a entrada do usuário e retorna em argumentos"""

    entry = input(f"{Colors.TITLE} > {Colors.TEXT}")
    
    if not entry:
        raise InvalidCommandError()

    return entry.split()

