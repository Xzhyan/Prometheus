from core.config import ALERT_SCHEMES, FG_TEXT


def alert(type, text):
    """Exibe alertas personalizados"""

    if type in ALERT_SCHEMES:
        color = ALERT_SCHEMES[type]
        print(f"{color}[{type}] {FG_TEXT}{text}")



def get_entry(text = None):
    """Função para receber entradas do usuário"""

    if not text:
        text = '<'

    entry = input(f"{text} > ")

    if not entry:
        print("Por favor digite alguma coisa!")

    entries = entry.split()

    return entries