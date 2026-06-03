
# core
from core.config import settings
from core.constants import Colors


class Banner:
    TOOL_LOGO = f"""{Colors.ONE}
                          ┏━┓┏━┓┏━┓┏┳┓┏━╸╺┳╸╻ ╻┏━╸╻ ╻┏━┓
                          ┣━┛┣┳┛┃ ┃┃┃┃┣╸  ┃ ┣━┫┣╸ ┃ ┃┗━┓
                          ╹  ╹┗╸┗━┛╹ ╹┗━╸ ╹ ╹ ╹┗━╸┗━┛┗━┛
                         {Colors.TITLE}Developed by {Colors.TEXT}{settings.AUTHOR} {Colors.TITLE}- ver: {Colors.TEXT}{settings.VERSION}
    """

    HELP_MENU = f"""
    Bem-vindo ao menu de ajuda ferramenta
    """
