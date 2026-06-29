# core
from core import settings
from core.logger import addlog
from core.constants import Colors

# ui
from ui.ui_console import alert


# utils/system
from utils.system import (
    shutdown,
    restart,
    set_title,
    clear,
    run_module,
    run_python_module,
    read_json,
    write_json
)


def easy_sharing():
    run_python_module(
        settings.EASY_PATH,
        'manage.py',
        'runserver',
        settings.EASY_SERVER_IP
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

            except Exception as e:
                addlog('error', str(e))
                alert('error', str(e))


def open_vscode():
    pass


def open_short(short):
    """Emula o comando cd para abrir atalhos adicionados"""

    pass


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
    'cd': {
        'desc': "acessa o caminho do atalho ex: cd meu_atalho",
        'handler': lambda short: open_short(short)
    },
    'code': {
        'desc': "abre o VS Code na pasta do atalho",
        'handler': open_vscode
    }
}


SPECIAL_COMMANDS = {
    'easy': {
        'desc': "inicia o EasySharing (ftp/drive local)",
        'handler': easy_sharing
    }
}
