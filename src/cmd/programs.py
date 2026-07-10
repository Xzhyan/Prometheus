from utils.system import read_json, write_json


class Programs:
    def __init__(self, *args):

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

        pass

    def add(self):
        pass

    def list_apps(self):
        pass

    def dispatch(self):
        pass


def run_app():
    """Abre aplicativos adicionados"""

    pass


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
