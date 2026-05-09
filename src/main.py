from core import settings

# utils/console
from utils.console import clear, title, close, entry

# ui/console
from ui.console import response

# Banners
from ui.banners import TOOL_BANNER


class Main:
    def __init__(self):
        clear()
        title(settings.TOOL_NAME)
        print(TOOL_BANNER)
        self.startup()


    def startup(self):
        while True:
            cmd = entry()

            if not cmd:
                continue

            if cmd[0] == 'exit':
                response('info', "Encerrando a ferramenta...")
                close()




if __name__ == '__main__':
    try:
        Main()

    except KeyboardInterrupt:
        response('info', "Encerrando a ferramenta...")
        close()
