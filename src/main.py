# core
from core import settings
from core.exceptions import InvalidCommandError, CommandNotFoundError
from core.logger import add_log

# ui
from ui.banners import Banner
from ui.ui_console import alert

# utils
from utils.system import entry

# commands
from commands.default import DEFAULT_COMMANDS, shutdown, clear



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

                if command == 'help':
                    print(Banner.HELP_MENU)

                elif command in DEFAULT_COMMANDS:
                    DEFAULT_COMMANDS[command]['handler']()

                else:
                    raise CommandNotFoundError()

            except InvalidCommandError as e:
                add_log('error', f"INVALID_COMMAND | {e}")
                alert('error', str(e))

            except CommandNotFoundError as e:
                add_log('error', f"COMMAND_NOT_FOUND | {e}")
                alert('error', str(e))
            
            except Exception as e:
                add_log('error', f"{type(e).__name__} | {e}")


if __name__ == '__main__':
    try:
        tool = Main()
        tool.startup()

    except KeyboardInterrupt:
        alert('info', "Finalizando...")
