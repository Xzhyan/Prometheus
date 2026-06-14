# core/config
from core import settings

# utils
from utils.system import shutdown, clear, run_module, run_module_with_command


def easy_sharing():
    run_module_with_command(
        settings.EASY_PATH,
        'manage.py',
        'runserver',
        settings.EASY_SERVER_IP
    )


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


SPECIAL_COMMANDS = {
    'easy': {
        'desc': "Inicia o EasySharing (ftp/drive local)",
        'handler': easy_sharing
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

