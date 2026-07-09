# core
from core import settings
from core.dependencies import check_all
from core.exceptions import InvalidCommandError, CommandNotFoundError, ShortNotFoundError
from core.logger import addlog

# ui
from ui.banners import Banners
from ui.ui_console import alert, list_commands

# utils
from utils.system import entry, set_title, shutdown, clear

# commands
from cmd.commands import DEFAULT_COMMANDS

# special commands
from cmd.specials import SPECIAL_COMMANDS


class Prometheus:
    def __init__(self):
        self.running = check_all()

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
                    DEFAULT_COMMANDS[command]['handler'](args)

                elif command in SPECIAL_COMMANDS:
                    SPECIAL_COMMANDS[command]['handler'](args)

                else:
                    raise CommandNotFoundError()

            except InvalidCommandError as e:
                addlog('error', f"INVALID_COMMAND | {e}")
                alert('error', str(e))

            except CommandNotFoundError as e:
                addlog('error', f"COMMAND_NOT_FOUND | {e}")
                alert('error', str(e))

            except ShortNotFoundError as e:
                addlog('error', f"SHORT_NOT_FOUND | {e}")
                alert('error', str(e))
            
            except IndexError:
                addlog('error', f"INDEX_ERROR | cmd={command} | argumentos faltando")
                alert('error', f"Faltam argumentos. Use help e leia o modo de uso do comando.")

            except Exception as e:
                addlog('error', f"{type(e).__name__} | {e}")
                alert('error', str(e))


if __name__ == '__main__':
    try:
        main = Prometheus()
        main.startup()

    except KeyboardInterrupt:
        alert('info', "Finalizando...")
