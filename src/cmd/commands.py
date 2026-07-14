import subprocess

# core
from core import settings
from core.logger import addlog
from core.constants import Colors, SHORTS_JSON
from core.dependencies import path_check
from core.exceptions import PathNotFoundError, ShortNotFoundError

# ui
from ui.ui_console import alert, list_commands

# utils/system
from utils.system import (
    shutdown,
    restart,
    clear,
    run_python_module,
)

# functions
from utils.functions import read_json, write_json


class CustomShort:
    def __init__(self, args):
        self.running = True

        self.commands = {
            'add': {
                'desc': "adiciona um novo atalho",
                'handler': self.add
            },
            'list': {
                'desc': "lista os atalhos adicionados",
                'handler': self.list
            }
        }

        self.manage()

    def add(self):
        type_ = input(' tipo app/dir > ')
        name = input(' nome do atalho > ')
        path = input(' caminho do atalho > ')

        if not type_ or not name or not path:
            print('campo vazio')

        data = read_json(SHORTS_JSON)

        for category, short in data.items():
            for short_name in short:
                if short_name['name'] == name:
                    alert('info', "já existe um atalho com esse nome")
                    return

        data[type_].append({
            'name': name,
            'path': path
        })

        write_json(SHORTS_JSON, data)

        alert('success', "atalho adicionado")

        self.running = False

    def list(self):
        data = read_json(SHORTS_JSON)

        # lista dos atalhos, para agrupar por categoria
        app = []
        dir = []

        for category, short in data.items():
            for short_name in short:
                if category == 'app':
                    app.append(short_name['name'])
                else:
                    dir.append(short_name['name'])
        
        print(app)
        print(dir)

        self.running = False

    def manage(self):
        while self.running:
            list_commands('Comandos do modulo de atalhos', self.commands)

            try:
                cmd = input(" \n custom short > ")

                if cmd in self.commands:
                    self.commands[cmd]['handler']()
                
                else:
                    self.running = False

            except Exception as e:
                response = str(e)
                
                addlog('error', f"UNKNOWN_ERROR | {response}")
                alert('error', response)
            
            except KeyboardInterrupt:
                self.running = False

                response = "modulo de atalhos finalizado..."

                addlog('info', f"SHORT_MODULE | {response}")
                alert('info', response)



DEFAULT_COMMANDS = {
    'exit': {
        'desc': "finalizar a ferramenta",
        'handler': shutdown
    },
    'restart': {
        'desc': "finaliza o processo atual e inicia um novo",
        'handler': restart
    },
    'clear': {
        'desc': "limpar a tela",
        'handler': clear
    },
    'short': {
        'desc': "inicia o modulo de atalhos",
        'handler': CustomShort
    }
}
