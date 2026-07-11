import subprocess

# core
from core.constants import Colors
from core.exceptions import AppNotFoundError, FilePathNotFoundError
from core.dependencies import file_check
from core.logger import addlog

# ui
from ui.ui_console import list_commands, alert

# utils
from utils.functions import read_json, write_json



class Programs:
    def __init__(self, *args):
        self.running = True

        self.commands = {
            'add': {
                'desc': "adiciona um aplicativo",
                'handler': self.add
            },
            'list': {
                'desc': "lista os aplicativos adicionados",
                'handler': self.list_apps
            }
        }

        self.manage_apps()

    def add(self):
        pass

    def list_apps(self):
        data = read_json('apps.json')

        print(f"\n{Colors.TITLE}[+] {Colors.TEXT}Lista de aplicativos {Colors.TITLE}")
        for app in data['apps']:
            print(f" {Colors.TEXT}↪ {Colors.TITLE}{app['name']}")

    def manage_apps(self):
        list_commands('Aplicativos', self.commands)

        while self.running:
            try:
                cmd = input(f"\n {Colors.TEXT} @apps {Colors.TITLE}>> {Colors.TEXT}")

                if cmd in self.commands:
                    self.commands[cmd]['handler']()

                else:
                    self.running = False

            except KeyboardInterrupt:
                print()
                alert('info', "Finalizando apps...")
                self.running = False


def run_app(args):
    """Abre aplicativos adicionados"""

    app_name = args[1]
    data = read_json('apps.json')
    file_path = None

    for app in data['apps']:
        if app['name'] == app_name:
            file_path = app['path']
            break

    if file_path is None:
        raise AppNotFoundError("O aplicativo não foi encontrado")

    try:
        file_check(file_path)
        subprocess.Popen(f'"{file_path}"')

    except FileNotFoundError as e:
        addlog('error', str(e))
        alert('error', str(e))

    except Exception as e:
        addlog('error', str(e))
        alert('error', str(e))


PROGRAMS_COMMANDS = {
    'apps': {
        'desc': "gerenciar aplicativos",
        'handler': Programs
    },
    'app': {
        'desc': "abre o aplicativo adicionado",
        'handler': lambda args: run_app(args)
    }
}
