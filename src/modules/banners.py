# Contantes
from core.config import TOOL_NAME, AUTHOR, VERSION

# Cores
from core.config import FG_TEXT, FG_TITLE, FG_ONE, FG_TWO, FG_SUCCESS, FG_ERROR, FG_INFO, FG_WARNING


def BANNER():
    return f"""{FG_ONE}
┏┓┳┓┏┓┳┳┓┏┓┏┳┓┓┏┏┓┳┳┏┓
┃┃┣┫┃┃┃┃┃┣  ┃ ┣┫┣ ┃┃┗┓
┣┛┛┗┗┛┛ ┗┗┛ ┻ ┛┗┗┛┗┛┗┛
Developed by {FG_TWO}{AUTHOR} {FG_ONE}<:> version: {FG_TWO}{VERSION}
    """