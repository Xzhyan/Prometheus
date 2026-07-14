import subprocess

# core
from core import settings
from core.logger import addlog
from core.constants import Colors
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
from utils.functions import (
    read_json,
    write_json
)


class CustomShort:
    def __init__(self, *args):
        self.running = True

        self.commands = {
            'add': {
                'desc': "adiciona novo atalho",
                'handler': self.add_short
            },
            'remove': {
                'desc': "remove um atalho",
                'handler': self.remove_short
            },
            'list': {
                'desc': "lista os atalhos adicionados",
                'handler': self.list_short
            },
            'update': {
                'desc': "atualiza um atalho",
                'handler': self.update_short
            }
        }

        self.manage_short()

    def add_short(self):
        name = input(f"   {Colors.TEXT}↪ {Colors.TITLE}nome do atalho: {Colors.TEXT}")
        path = input(f"   {Colors.TEXT}↪ {Colors.TITLE}caminho do atalho: {Colors.TEXT}")

        if not name or not path:
            alert('error', "você deixou um campo vazio")
            return

        data = read_json('shorts.json')

        for short in data['shorts']:
            if short['name'] == name:
                alert('info', "já existe um atalho com o mesmo nome")
                return

        data['shorts'].append({
            'name': name,
            'path': path
        })

        write_json('shorts.json', data)

        alert('success', "atalho adicionado")
        self.running = False

    def list_short(self):
        data = read_json('shorts.json')

        print(f"\n{Colors.TITLE}[+] {Colors.TEXT}Lista de atalhos {Colors.TITLE}")
        for short in data['shorts']:
            print(f" {Colors.TEXT}↪ {Colors.TITLE}{short['name']}")

    def remove_short(self):
        name = input(f"   {Colors.TEXT}↪ {Colors.TITLE}nome do atalho: {Colors.TEXT}")

        if not name:
            alert('error', 'o nome do atalho deve ser informado')
        
        data = read_json('shorts.json')
        
        try:
            for short in data['shorts']:
                if short['name'] == name:
                    data['shorts'].remove(short)

                    addlog('error', "atalho removido com sucesso")
                    alert('success', "atalho removido com sucesso")
                    break
        
        except Exception as e:
            alert('error', str)

    def update_short(self):
        pass

    def manage_short(self):
        list_commands('shorts', self.commands)
        while self.running:
            try:
                cmd = input(f"\n {Colors.TEXT} @shorts {Colors.TITLE}>> {Colors.TEXT}")

                if cmd in self.commands:
                    self.commands[cmd]['handler']()

                else:
                    self.running = False
            
            except KeyboardInterrupt:
                print()
                alert('info', "Finalizando shorts...")
                self.running = False

            except Exception as e:
                addlog('error', str(e))
                alert('error', str(e))


def open_short(args):
    """Abre os atalhos adicionados no explorer ou no vs code"""

    cmd = 'code' if args[0] == 'code' else 'start'

    short_name = args[1]
    data = read_json('shorts.json')
    path = None

    for short in data['shorts']:
        if short['name'] == short_name:
            path = short['path']
            break

    if path is None:
        raise ShortNotFoundError("O atalho não existe")

    try:
        path_check(path)
        subprocess.Popen(f'{cmd} "" "{path}"', shell=True)

    except PathNotFoundError as e:
        addlog('error', str(e))
        alert('error', str(e))


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
    'shorts': {
        'desc': "gerenciar os atalhos",
        'handler': CustomShort
    },
    'open': {
        'desc': "abre o Explorer na pasta do atalho",
        'handler': lambda args: open_short(args)
    },
    'code': {
        'desc': "abre o VS Code na pasta do atalho",
        'handler': lambda args: open_short(args)
    }
}
