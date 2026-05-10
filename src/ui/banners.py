from core import settings
from core.constants import Colors


TOOL_BANNER = f"""{Colors.PRIMARY}
                        ┌─┐┌─┐┌─┐┌┬┐┌─╴╶┬╴╷ ╷┌─╴╷ ╷┌─┐
                        ├─┘├┬┘│ ││││├╴  │ ├─┤├╴ │ │└─┐
                        ╵  ╵└╴└─┘╵ ╵└─╴ ╵ ╵ ╵└─╴└─┘└─┘
                Developed by {Colors.TEXT}{settings.AUTHOR} {Colors.TITLE}- version: {Colors.TEXT}{settings.VERSION}
"""


HELP_BANNER = f"""{Colors.PRIMARY}
┌────────────────────────────────────────────────────┐
│     Bem-vindo ao menu de ajuda da ferramenta       │
│                                                    │
│ {Colors.TEXT}Lista de comandos:{Colors.PRIMARY}                                 │
│                                                    │
│ {Colors.SUCCESS}exit {Colors.PRIMARY}>> {Colors.TEXT}Encerra a ferramenta                       {Colors.PRIMARY}│
│ {Colors.SUCCESS}clear {Colors.PRIMARY}>> {Colors.TEXT}Limpa a tela da ferramenta                {Colors.PRIMARY}│
│ {Colors.SUCCESS}shortcut {Colors.PRIMARY}>> {Colors.TEXT}Lista de comandos de atalhos           {Colors.PRIMARY}│
└────────────────────────────────────────────────────┘
"""

