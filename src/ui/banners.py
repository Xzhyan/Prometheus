# core
from core.config import settings
from core.constants import Colors


class Banners:
    TOOL_LOGO = f"""{Colors.TITLE}
                            ┏┓┳┓┏┓┳┳┓┏┓┏┳┓┓┏┏┓┳┳┏┓
                            ┃┃┣┫┃┃┃┃┃┣  ┃ ┣┫┣ ┃┃┗┓
                            ┣┛┛┗┗┛┛ ┗┗┛ ┻ ┛┗┗┛┗┛┗┛
                        {Colors.TEXT}Developed by {Colors.TITLE}{settings.AUTHOR} {Colors.TEXT}- ver: {Colors.TITLE}{settings.VERSION}"""

    HELP_MENU = f"""{Colors.TEXT}
               Bem-vindo ao menu de ajuda da ferramenta {Colors.TITLE}{settings.TOOL_NAME}{Colors.TEXT}
        Essa ferramenta tem por finalidade automatizar tarefas do Windows
             Auxiliando o usuário e melhorando seu rítmo de produção;"""
