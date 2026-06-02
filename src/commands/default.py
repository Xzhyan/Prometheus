from utils.console import shutdown, clear


DEFAULT_COMMANDS = {
    'exit': {
        'desc': "Finalizar a ferramenta",
        'run': shutdown
    },
    'clear': {
        'desc': "Limpar a tela",
        'run': clear
    }
}
