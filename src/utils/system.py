import subprocess, platform, sys, json
from pathlib import Path

# core, exceptions, dependencies, logger
from core import settings
from core.constants import Colors, USERNAME, BASE_DIR
from core.exceptions import InvalidCommandError, PathNotFoundError, FilePathNotFoundError
from core.dependencies import file_check, path_check
from core.logger import addlog

# ui
from ui.ui_console import alert


def shutdown():
    """Finalizar a ferramenta"""

    alert('info', "Finalizando...")
    sys.exit(0)


def restart():
    """Reinicia a ferramenta"""

    run_module('src', 'main.py')
    shutdown()


def clear():
    """Limpa a tela da ferramenta"""

    cmd = 'cls' if platform.system() == 'Windows' else 'clear'
    subprocess.run(cmd, shell=True)


def set_title(title):
    """Seta um titulo pra janela da ferramenta"""

    if platform.system() == 'Windows':
        subprocess.run(f'title {title}', shell=True)


def entry():
    """Recebe a entrada do usuário e retorna em argumentos"""

    print(f"\n {Colors.ONE}┌┄({Colors.TEXT}{settings.TOOL_NAME}{Colors.ONE})-[{Colors.TEXT}{USERNAME}{Colors.ONE}]")
    entry = input(f" {Colors.TITLE}└┄┄┄⎶›{Colors.TEXT} ")
    
    if not entry:
        raise InvalidCommandError()

    return entry.split()


def run_module(path, name):
    module = BASE_DIR / path / name

    try:
        file_check(module)
        
        subprocess.Popen(
            [sys.executable, str(module)],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

    except FilePathNotFoundError as e:
        addlog('error', str(e))
        alert('error', str(e))

    except Exception as e:
        addlog('error', str(e))


def run_python_module(path, *args):
    try:
        path = Path(path)
        path_check(path)
        python_venv = path / '.venv' / 'Scripts' / 'python.exe'
        
        subprocess.Popen(
            [str(python_venv), *args],
            cwd=path,
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

    except FilePathNotFoundError as e:
        addlog('error', str(e))
        alert('error', str(e))

    except Exception as e:
        addlog('error', str(e))


def read_json(json_file):
    """Função para ler arquivo json"""

    try:
        with open(BASE_DIR / 'json' / json_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    except Exception as e:
        print(str(e))


def write_json(json_file, data):
    """Escreve no arquivo json"""

    try:
        with open(BASE_DIR / 'json' / json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
    except Exception as e:
        print(str(e))