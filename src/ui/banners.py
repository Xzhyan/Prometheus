# core
from core.config import settings
from core.constants import Colors


class Banners:
    TOOL_LOGO = f"""{Colors.TITLE}
                  {Colors.TITLE}Developed by {Colors.TEXT}{settings.AUTHOR} {Colors.TITLE}- team {Colors.TEXT}{settings.TEAM} {Colors.ONE}
                    ┏┓  ┳┓  ┏┓  ┳┳┓  ┏┓  ┏┳┓  ┓┏  ┏┓  ┳┳  ┏┓
                    ┃┃  ┣┫  ┃┃  ┃┃┃  ┣    ┃   ┣┫  ┣   ┃┃  ┗┓
                    ┣┛  ┛┗  ┗┛  ┛ ┗  ┗┛   ┻   ┛┗  ┗┛  ┗┛  ┗┛
                                                    {Colors.TITLE}ver: {Colors.TEXT}{settings.VERSION}"""

    HELP_MENU = f"""{Colors.TEXT}
               Bem-vindo ao menu de ajuda da ferramenta {Colors.TITLE}{settings.TOOL_NAME}{Colors.TEXT}
        Essa ferramenta tem por finalidade automatizar tarefas do Windows
             Auxiliando o usuário e melhorando seu rítmo de produção;"""
