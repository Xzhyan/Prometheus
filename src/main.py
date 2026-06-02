# core
from core import settings
from core.exceptions import InvalidCommandError

# ui
from ui.banners import Banner
from ui.ui_console import alert

# utils
from utils.console import shutdown, clear, entry



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

                if command == 'exit':
                    self.running = shutdown()

                else:
                    raise InvalidCommandError()

            except InvalidCommandError as e:
                alert('error', str(e))



if __name__ == '__main__':
    try:
        tool = Main()
        tool.startup()

    except KeyboardInterrupt:
        alert('info', "Finalizando...")
