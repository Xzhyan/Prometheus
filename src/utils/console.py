import subprocess, platform, sys

# core/constants
from core.constants import Colors

# ui/console
from ui.console import ENTRY


def clear():
    """Limpa a tela da ferramenta"""
    
    cmd = 'cls' if platform.system() == 'Windows' else 'clear'
    subprocess.run(cmd, shell=True)


def title(text):
    """Seta o titulo da ferramenta"""
    if platform.system() == 'Windows':
        cmd = f'title {text}'


def close():
    """Encerra a ferramenta"""

    sys.exit()


def entry():
    """Recebe entradas do usuário"""
    
    try:
        print(ENTRY)
        get_entry = input("    > ")

        if not get_entry:
            return None
        
        return get_entry.split()
    
    except KeyboardInterrupt:
        return ['exit']

    except EOFError:
        return ['exit']
