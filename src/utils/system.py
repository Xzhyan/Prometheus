import subprocess, platform, sys
from pathlib import Path

# core, exceptions, dependencies, logger
from core import settings
from core.constants import Colors, USERNAME, BASE_DIR
from core.exceptions import InvalidCommandError, PathNotFoundError, FilePathNotFoundError
from core.dependencies import file_check, path_check
from core.logger import add_log

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

    print(f"\n {Colors.ONE}┌─({Colors.TEXT}{settings.TOOL_NAME}{Colors.ONE})-[{Colors.TEXT}{USERNAME}{Colors.ONE}]")
    entry = input(f" {Colors.TITLE}└⇘⇘⇘ {Colors.TEXT}")
    
    if not entry:
        raise InvalidCommandError()

    return entry.split()


def list_commands(category):
    """Faz a lsitagem dos comandos"""

    for cmd, data in category.items():
        print(f"    {Colors.TITLE}{cmd} {Colors.TEXT}-> {data['desc']}")


def run_module(path, name):
    module = BASE_DIR / path / name

    try:
        file_check(module)
        
        subprocess.Popen(
            [sys.executable, str(module)],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

    except FilePathNotFoundError as e:
        add_log('error', str(e))
        alert('error', str(e))

    except Exception as e:
        add_log('error', str(e))


# modelo para run module admin e verificador
# def run_module_admin(module):
#     ctypes.windll.shell32.ShellExecuteW(
#         None,
#         "runas",
#         sys.executable,
#         str(module),
#         None,
#         1
#     )

# import ctypes

# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False
