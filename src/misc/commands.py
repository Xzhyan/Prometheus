# utils
from utils.system import shutdown, clear, run_module


def ids():
    run_module('defense/ids', 'main.py')


def port_scan():
    run_module('src/misc/cybersec', 'portscan.py')


DEFAULT_COMMANDS = {
    'exit': {
        'desc': "Finalizar a ferramenta",
        'handler': shutdown
    },
    'clear': {
        'desc': "Limpar a tela",
        'handler': clear
    }
}


CYBERSEC_COMMANDS = {
    'portscan': {
        'desc': "Escaner de portas",
        'handler': port_scan
    },
    'ids': {
        'desc': "Sistema de detecção de intrusão",
        'handler': ids
    }
}

