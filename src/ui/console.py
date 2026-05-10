from core import settings
from core.constants import Colors, RESPONSE_DICT


# Estilização do entry de entra de comandos do usuario
ENTRY = f"{Colors.PRIMARY}┌─({Colors.SECONDARY}{settings.TOOL_NAME}{Colors.PRIMARY})-[] \n{Colors.PRIMARY}└⇘⇘⇘"


def response(res_type, text):
    """Resposta personaliza por tipos (erro, sucesso, info)"""

    res_type_color = RESPONSE_DICT.get(res_type.lower(), Colors.TEXT)

    print(f'{res_type_color}[{res_type.upper()}] ⇒ {Colors.TEXT}{text}')


