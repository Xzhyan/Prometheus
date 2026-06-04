
# core
from core.config import settings
from core.constants import Colors


class Banner:
    TOOL_LOGO = f"""{Colors.ONE}
                          ┏━┓┏━┓┏━┓┏┳┓┏━╸╺┳╸╻ ╻┏━╸╻ ╻┏━┓
                          ┣━┛┣┳┛┃ ┃┃┃┃┣╸  ┃ ┣━┫┣╸ ┃ ┃┗━┓
                          ╹  ╹┗╸┗━┛╹ ╹┗━╸ ╹ ╹ ╹┗━╸┗━┛┗━┛
                         {Colors.TITLE}Developed by {Colors.TEXT}{settings.AUTHOR} {Colors.TITLE}- ver: {Colors.TEXT}{settings.VERSION}"""

    HELP_MENU = f"""
    Bem-vindo ao menu de ajuda da ferramenta {settings.TOOL_NAME}

    A ferramenta foi desenvolvida para automatizar tarefas na plataforma Windows, disponibilizar funcionalidades avançadas e futuramente ter recursos para segurança cibernética.
    
    Lista de comandos: (obs: estão separados por categorias)

    """
