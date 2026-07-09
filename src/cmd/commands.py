import subprocess

# core
from core import settings
from core.logger import addlog
from core.constants import Colors
from core.dependencies import path_check
from core.exceptions import PathNotFoundError, ShortNotFoundError

# ui
from ui.ui_console import alert

# utils/system
from utils.system import (
    shutdown,
    restart,
    clear,
    run_python_module,
    read_json,
    write_json
)


class CustomShort:
    def __init__(self, *args):
        self.running = True

        self.commands = {
            'add': self.add_short,
            'remove': self.remove_short,
            'list': self.list_short,
            'update': self.update_short
        }

        self.manage_short()

    def entry(self):
        name = input(" nome do atalho: ")
        path = input(" caminho do atalho: ")

        return name, path

    def add_short(self):
        name, path = self.entry()

        if not name or not path:
            alert('error', "Você deixou um campo vazio")
            return

        data = read_json('shorts.json')

        for short in data['shorts']:
            if short['name'] == name:
                alert('info', "Já existe um atalho com o mesmo nome")
                return

        data['shorts'].append({
            'name': name,
            'path': path
        })

        write_json('shorts.json', data)

        alert('success', "Atalho adicionado")
        self.running = False

    def remove_short(self):
        pass

    def list_short(self):
        data = read_json('shorts.json')

        print(f"\n{Colors.TITLE}[+] {Colors.TEXT}Lista de atalhos {Colors.TITLE}")
        for short in data['shorts']:
            print(f" {Colors.TEXT}↪ {Colors.TITLE}{short['name']}")

    def update_short(self):
        pass

    def manage_short(self):
        while self.running:
            try:
                cmd = input(f" \n{Colors.TEXT}opções: [ {Colors.TITLE}add {Colors.TEXT}| {Colors.TITLE}remove {Colors.TEXT}| {Colors.TITLE}list {Colors.TEXT}| {Colors.TITLE}update {Colors.TEXT}] > ")

                if cmd in self.commands:
                    self.commands[cmd]()

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
        subprocess.run(f'{cmd} "" "{path}"', shell=True)

    except PathNotFoundError as e:
        addlog('error', str(e))
        alert('error', str(e))


def browser_start(args):
    """Abre o navegador configurado por padrão já na página do google.com"""

    subprocess.run('start https://google.com', shell=True)


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
    },
    'browser': {
        'desc': "abre o nevegador padrão já na página do google.com",
        'handler': browser_start
    }
}
