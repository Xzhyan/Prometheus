# core
from core import settings
from core.exceptions import InvalidCommandError, CommandNotFoundError

# ui
from ui.banners import Banner
from ui.ui_console import alert

# utils
from utils.console import shutdown, clear, entry

# commnds
from commands.default import DEFAULT_COMMANDS



class Main:
    def __init__(self):
        self.running = True
    
    def startup(self):
        clear()
        print(Banner.TOOL_LOGO)
        self.dispatch()
    
    def dispatch(self):
        while self.running:
            try:
                args = entry()
                command = args[0]

                if command in DEFAULT_COMMANDS:
                    DEFAULT_COMMANDS[command]['run']()

                else:
                    raise CommandNotFoundError()

            except InvalidCommandError as e:
                alert('error', str(e))

            except CommandNotFoundError as e:
                alert('error', str(e))


if __name__ == '__main__':
    try:
        tool = Main()
        tool.startup()

    except KeyboardInterrupt:
        alert('info', "Finalizando...")
