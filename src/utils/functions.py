import json

# core
from core.dependencies import file_check
from core.constants import BASE_DIR, JSON_DIR
from core.exceptions import FilePathNotFoundError
from core.logger import addlog

# ui
from ui.ui_console import alert


def read_json(json_file):
    """Função para ler arquivo json"""

    try:
        json_path = JSON_DIR / json_file
        file_check(json_path)

        with open(BASE_DIR / 'json' / json_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    except FilePathNotFoundError:
        addlog('error', str(e))
        alert('error', str(e))

    except Exception as e:
        addlog('error', str(e))
        print(str(e))


def write_json(json_file, data):
    """Escreve no arquivo json"""

    try:
        json_path = BASE_DIR / 'json' / json_file
        file_check(json_path)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    except FilePathNotFoundError:
        addlog('error', str(e))
        alert('error', str(e))
        
    except Exception as e:
        addlog('error', str(e))
        alert('error', str(e))
