
# core
from core.config import settings
from core.constants import Colors


class Banner:
    TOOL_LOGO = f"""{Colors.ONE}
                          ┏━┓┏━┓┏━┓┏┳┓┏━╸╺┳╸╻ ╻┏━╸╻ ╻┏━┓
                          ┣━┛┣┳┛┃ ┃┃┃┃┣╸  ┃ ┣━┫┣╸ ┃ ┃┗━┓
                          ╹  ╹┗╸┗━┛╹ ╹┗━╸ ╹ ╹ ╹┗━╸┗━┛┗━┛
                         {Colors.TEXT}Developed by {Colors.TITLE}{settings.AUTHOR} {Colors.TEXT}- ver: {Colors.TITLE}{settings.VERSION}"""

    HELP_MENU = f"""{Colors.TEXT}
    Bem-vindo ao menu de ajuda da ferramenta {Colors.TITLE}{settings.TOOL_NAME}{Colors.TEXT}

    A ferramenta foi desenvolvida para automatizar tarefas no OS Windows;
    Disponibilizar funcionalidades avançadas; e
    Futuramente ter recursos para segurança cibernética;
    
    Lista de comandos:"""
