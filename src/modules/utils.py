
# Contantes
from core.config import ALERT_SCHEMES, AUTHOR, TOOL_NAME

# Colors
from core.config import FG_TEXT, FG_ONE, FG_TWO

def alert(type_alert, text):
    """Exibe alertas personalizados"""

    if type_alert in ALERT_SCHEMES:
        color = ALERT_SCHEMES[type_alert]
        print(f"{color}[{type_alert.upper()}] {FG_TEXT}{text}")



def get_entry(text = None):
    """Recebe as entradas do usuário"""

    if not text:
        text = ''
    
    print(f'{FG_ONE}┌─({FG_TWO}{TOOL_NAME}{FG_ONE})~[{FG_TWO}{AUTHOR}{FG_ONE}]')
    entry = input(f"└───> {text} < {FG_TWO}")

    if not entry:
        alert('error', "Por favor informe um comando válido ou digite 'help'")

    entries = entry.split()

    return entries