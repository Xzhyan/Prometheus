import subprocess, platform, sys, os

# core/constants
from core.constants import Colors, BASE_DIR

# ui/console
from ui.console import ENTRY

# core/excpetions
from core.exceptions import PathNotFoundError


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
        get_entry = input(f"    > {Colors.TEXT}")

        if not get_entry:
            return None
        
        return get_entry.split()
    
    except KeyboardInterrupt:
        return ['exit']

    except EOFError:
        return ['exit']


def verify_path(path):
    """Verifica a existencia de paths"""

    if not os.path.exists(path):
        raise PathNotFoundError(path)


def run_subprocess(path):
    py_path = os.path.join('.venv', 'Scripts', 'python.exe')

    try:
        verify_path(path)
        verify_path(py_path)

        abs_path = os.path.abspath(path)

        subprocess.Popen(
            [py_path, abs_path],
            cwd=os.path.dirname(abs_path),
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

    except PathNotFoundError as e:
        print(f"\n{e}\n")

    except FileNotFoundError as e:
        print(f"\nArquivo não encontado: \n{e}\n")

    except OSError as e:
        print(f"\nErro do sistema: \n{e}\n")
    
    except Exception as e:
        print(f"\nErro desconhecido: \n{e}\n")
