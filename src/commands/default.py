from utils.console import close, clear

# ui
from ui.banners import HELP_BANNER
from ui.console import list_commands

# commands
from .shortcut import SHORTCUT_COMMANDS


def help_menu():
    print(HELP_BANNER)


DEFAULT_COMMANDS = {
    'exit': {
        'func': close,
        'desc': "Encerra a ferramenta"
    },
    'clear': {
        'func': clear,
        'desc': "Limpa a tela da ferramenta"
    },
    'help': {
        'func': help_menu,
        'desc': "Exibe o menu de ajuda"
    },
    'shortcut': {
        'func': lambda: list_commands(SHORTCUT_COMMANDS),
        'desc': "Lista de comandos de atalhos"
    },
}
