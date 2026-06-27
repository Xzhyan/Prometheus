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


def list_commands(name, category):
    """Faz a lsitagem dos comandos"""

    print(f"\n{Colors.TEXT}[+] {Colors.ONE}{name}")
    for cmd, data in category.items():
        print(f" {Colors.TEXT}↪ {Colors.TITLE}{cmd} {Colors.TEXT}-> {data['desc']}")
