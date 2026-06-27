# core
from core import settings
from core.exceptions import InvalidCommandError, CommandNotFoundError
from core.logger import addlog

# ui
from ui.banners import Banners
from ui.ui_console import alert

# utils
from utils.system import entry, list_commands

# commands
from cmd.commands import (
    DEFAULT_COMMANDS,
    SPECIAL_COMMANDS,
    shutdown,
    set_title,
    clear
)


class Prometheus:
    def __init__(self):
        self.running = True
    
    def startup(self):
        clear()
        set_title("Prometheus")
        print(Banners.TOOL_LOGO)
        self.dispatch()
    
    def dispatch(self):
        while self.running:
            try:
                args = entry()
                command = args[0]

                if command == 'help':
                    clear()
                    print(Banners.HELP_MENU)
                    list_commands('Comandos normais', DEFAULT_COMMANDS)
                    list_commands('Comandos especiais', SPECIAL_COMMANDS)

                elif command in DEFAULT_COMMANDS:
                    DEFAULT_COMMANDS[command]['handler']()

                elif command in SPECIAL_COMMANDS:
                    SPECIAL_COMMANDS[command]['handler']()

                else:
                    raise CommandNotFoundError()

            except InvalidCommandError as e:
                addlog('error', f"INVALID_COMMAND | {e}")
                alert('error', str(e))

            except CommandNotFoundError as e:
                addlog('error', f"COMMAND_NOT_FOUND | {e}")
                alert('error', str(e))
            
            except Exception as e:
                addlog('error', f"{type(e).__name__} | {e}")


if __name__ == '__main__':
    try:
        main = Prometheus()
        main.startup()

    except KeyboardInterrupt:
        alert('info', "Finalizando...")
