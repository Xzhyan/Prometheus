from core.constants import Colors


def alert(type_, message):
    """Exibe mensagem de alerta na ferramenta"""

    colors = {
        'success': Colors.SUCCESS,
        'error': Colors.ERROR,
        'info': Colors.INFO,
        'warning': Colors.WARNING,
    }
    
    color = colors.get(type_, Colors.TEXT)

    print(f'{color}[{type_.upper()}] {Colors.TEXT}- {message}')


# def help_menu():
#     """Exibe o menu de ajuda da ferramenta"""

#     # importa os comando de forma local
#     from commands.default import DEFAULT_COMMANDS

#     for cmd, data in DEFAULT_COMMANDS.items():
#         print(f"{cmd} - {data['desc']}")
