import subprocess, os

# utils/console
from utils.console import verify_path

# core/exceptions
from core.exceptions import PathNotFoundError


def easy_sharing():
    """Inicializa o EasySharing"""

    easy_path = r'C:\Xzhyan\Workspace\webdev\EasySharing'
    py_path = os.path.join(easy_path, '.venv', 'Scripts', 'python.exe')

    try:
        verify_path(easy_path)
        verify_path(py_path)

        subprocess.Popen(
            [py_path, 'manage.py', 'runserver', '192.168.3.33:8000'],
            cwd=easy_path,
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


SHORTCUT_COMMANDS = {
    'easy': {
        'func': easy_sharing,
        'desc': "Inicia o EasySharing na rede doméstica"
    },
}

