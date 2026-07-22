import os, shutil, subprocess, sys, ctypes, time
from colorama import init
from pathlib import Path


# corrige o problema de cores do colorama no alert
init()

# caminho base para corrigir o problema de imports
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))


# core
from core.constants import USERNAME
from core.dependencies import path_check
from core.exceptions import PathNotFoundError

# ui
from ui.ui_console import alert


def clear_temp_files():
    """Limpa as pastas de arquivos temporários do sistema"""

    prefetch = f"C:\\Windows\\Prefetch"
    temp1 = f"C:\\Users\\{USERNAME}\\AppData\\Local\\Temp"
    temp2 = f"C:\\Windows\\temp"
    recent = f"C:\\Users\\{USERNAME}\\Recent"

    path_list = [temp2, prefetch, temp1, recent]

    try:
        for path in path_list:
            path_check(path)

            listed = os.listdir(path)

            for item in listed:
                item_path = os.path.join(path, item)

                try:
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                        alert('success', f"{item_path}: arquivo deletado com sucesso!", False)

                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                        alert('success', f"{item_path}: pasta deletada com sucesso!", False)

                except PermissionError as e:
                    alert('error', f"{e}: acesso negado")
                    continue

    except PathNotFoundError as e:
        alert('error', str(e))

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    try:
        clear_temp_files()

        alert('info', "Finalizando em alguns segundos...")

        time.sleep(10)
        sys.exit()

    except KeyboardInterrupt:
        alert('info', "Finalizando...")
