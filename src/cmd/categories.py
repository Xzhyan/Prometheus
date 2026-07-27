# ui
from ui.ui_console import list_commands

# commands
from .defaults import DEFAULT_COMMANDS
from .specials import SPECIAL_COMMANDS
from .selfdefense import SELF_DEFENSE


def list_defaults(*args):
    list_commands('Comandos Básicos', DEFAULT_COMMANDS)


def list_specials(*args):
    list_commands('Comandos Especiais', SPECIAL_COMMANDS)


def list_self_defense(*args):
    list_commands('Comandos de Auto-defesa', SELF_DEFENSE)


CATEGORIES = {
    'defaults': {
        'desc': "lista os comandos básicos",
        'handler': list_defaults 
    },
    'specials': {
        'desc': "lista os comandos especiais",
        'handler': list_specials
    },
    'self-defense': {
        'desc': "lista os comandos de auto-defesa",
        'handler': list_self_defense
    }
}
