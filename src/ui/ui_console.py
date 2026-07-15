from core.constants import Colors


def alert(type_, message, br=True):
    """Exibe mensagem de alerta na ferramenta"""

    colors = {
        'success': Colors.SUCCESS,
        'error': Colors.ERROR,
        'info': Colors.INFO,
        'warning': Colors.WARNING,
    }
    
    color = colors.get(type_, Colors.TEXT)

    # funciona como uma quebra de linha do alert
    if br:
        print()

    print(f'{color}[{type_.upper()}] {Colors.TEXT}- {message}')


def list_commands(name, category):
    """Faz a listagem dos comandos"""

    print(f"\n{Colors.TEXT}[+] {Colors.ONE}{name}")
    for cmd, data in category.items():
        print(f" {Colors.TEXT}↪ {Colors.TITLE}{cmd} {Colors.TEXT}-> {data['desc']}")
