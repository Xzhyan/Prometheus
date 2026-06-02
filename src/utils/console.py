import subprocess, platform, sys


def clear():
    """Limpa a tela da ferramenta"""

    cmd = 'cls' if platform.system() == 'Windows' else 'clear'
    subprocess.run(cmd, shell=True)

