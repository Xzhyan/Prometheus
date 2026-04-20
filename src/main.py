import subprocess


# Funções de utils
from src.modules.utils import get_entry, alert

# Banners
from src.modules.banners import BANNER

class Prometheus:
    def __init__(self):
        subprocess.run("title Prometheus CLI && cls", shell=True)
        print(BANNER())

        self.decision()

    def decision(self):
        """Loop principal e decisão dos comandos"""
        while True:
            entries = get_entry()

            print(entries)


if __name__ == '__main__':
    try:
        Prometheus()
    except KeyboardInterrupt:
        alert('info', "Saindo...")