

def list_commands(category):
    """Lista os comandos"""

    for cmd, data in category.items():
        print(f"{cmd} -> {data['desc']}")

