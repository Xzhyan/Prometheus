# core/config
from core import settings

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
    def __init__(self):
        self.running = True

        self.commands = {
            'add': self.add_short,
            'remove': self.remove_short,
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
            print("Você deixou campos vazios")
            return

        data = read_json('shorts.json')

        for short in data['shorts']:
            if short['name'] == name:
                print("Já existe um atalho com o mesmo nome")
                return

        data['shorts'].append({
            'name': name,
            'path': path
        })

        write_json('shorts.json', data)

        print("Atalho adicionado")
        self.running = False

    def remove_short(self):
        pass

    def update_short(self):
        pass

    def manage_short(self):
        while self.running:
            try:
                cmd = input(" opções: add / remove / update > ")

                if cmd in self.commands:
                    self.commands[cmd]()

                else:
                    self.running = False

            except Exception as e:
                print(str(e))


def open_vscode():
    pass


DEFAULT_COMMANDS = {
    'exit': {
        'desc': "Finalizar a ferramenta",
        'handler': shutdown
    },
    'restart': {
        'desc': "Finaliza o processo atual e inicia um novo",
        'handler': restart
    },
    'clear': {
        'desc': "Limpar a tela",
        'handler': clear
    },
    'short': {
        'desc': "Gerenciar os atalhos",
        'handler': CustomShort
    },
    'code': {
        'desc': "Abre o VS Code na pasta do atalho",
        'handler': open_vscode
    }
}


SPECIAL_COMMANDS = {
    'easy': {
        'desc': "Inicia o EasySharing (ftp/drive local)",
        'handler': easy_sharing
    }
}
