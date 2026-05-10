from core import settings
from core.constants import Colors, RESPONSE_DICT


# Estilização do entry de entrada de comandos do usuario
ENTRY = f"{Colors.PRIMARY}┌─({Colors.SECONDARY}{settings.TOOL_NAME}{Colors.PRIMARY})-[] \n{Colors.PRIMARY}└⇘⇘⇘"


def response(res_type, text):
    """Resposta personaliza por tipos (erro, sucesso, info)"""

    res_type_color = RESPONSE_DICT.get(res_type.lower(), Colors.TEXT)

    print(f'\n{res_type_color}[{res_type.upper()}] {Colors.PRIMARY}>> {Colors.TEXT}{text}\n')


def list_commands(category):
    """Lista os comandos por categoria"""

    for cmd, data in category.items():
        print(f'\n{Colors.SUCCESS}{cmd} {Colors.PRIMARY}>> {Colors.TEXT}{data['desc']}\n')

