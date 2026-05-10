from utils.console import close, clear


DEFAULT_COMMANDS = {
    'exit': {
        'func': close,
        'desc': "Encerra a ferramenta"
    },
    'clear': {
        'func': clear,
        'desc': "Limpa a tela da ferramenta"
    },
}

