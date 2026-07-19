import os, shutil

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

    path_list = [prefetch, temp1, temp2, recent]

    try:
        for path in path_list:
            path_check(path)

            listed = os.listdir(path)

            for item in listed:
                item_path = os.path.join(path, item)

                if os.path.isfile(item_path):
                    try:
                        os.remove(item_path)
                        alert('success', f"{item_path}: arquivo deletado com sucesso!", False)

                    except Exception as e:
                        print(str(e))

                elif os.path.isdir(item_path):
                    try:
                        shutil.rmtree(item_path)
                        alert('success', f"{item_path}: pasta deletada com sucesso!", False)

                    except Exception as e:
                        print(str(e))

    except PathNotFoundError as e:
        alert('error', str(e))

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    try:
        clear_temp_files()

    except KeyboardInterrupt:
        alert('info', "Finalizando...")
