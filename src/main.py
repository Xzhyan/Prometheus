from core import settings

# utils/console
from utils.console import clear, title, close, entry

# ui/console
from ui.console import response

# ui/banners
from ui.banners import TOOL_BANNER

# commnds
from commands.default import DEFAULT_COMMANDS
from commands.shortcut import SHORTCUT_COMMANDS
from commands.downloaders import DOWNLOADERS_COMMANDS


class Main:
    def __init__(self):
        clear()
        title(settings.TOOL_NAME)
        print(TOOL_BANNER)

        # Onde os comandos vão ser de fato expedidos
        self.dispatch()


    def dispatch(self):
        """Faz a expedição dos comandos"""

        while True:
            args = entry()

            if not args:
                continue

            cmd = args[0]

            if cmd in DEFAULT_COMMANDS:
                DEFAULT_COMMANDS[cmd]['func']()

            elif cmd in SHORTCUT_COMMANDS:
                SHORTCUT_COMMANDS[cmd]['func']()

            elif cmd in DOWNLOADERS_COMMANDS:
                DOWNLOADERS_COMMANDS[cmd]['func']()

            else:
                response('error', "Comando inexistente")


if __name__ == '__main__':
    try:
        Main()

    except KeyboardInterrupt:
        response('info', "Encerrando a ferramenta...")
        close()
