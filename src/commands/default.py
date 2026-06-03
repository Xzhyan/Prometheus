from utils.system import shutdown, clear


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

