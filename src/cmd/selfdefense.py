import subprocess

# core
from core.config import settings

# ui
from ui.ui_console import alert

def bit_defender(*args):
    """Abre o navegador padrão no site do bitdefender link checker"""

    try:
        url = settings.BIT_LINK_CHECKER_URL
        subprocess.Popen(f'start {url}', shell=True)

    except Exception as e:
        alert('error', str(e))


def virus_total(*args):
    """Abre o navegador padrão no site do virus total"""

    try:
        url = settings.VIRUS_TOTAL_URL
        subprocess.Popen(f'start {url}', shell=True)

    except Exception as e:
        alert('error', str(e))


SELF_DEFENSE = {
    'link-checker': {
        'desc': "Bitdefender: verificador de link malicioso",
        'handler': bit_defender
    },
    'virus-total': {
        'desc': "VirusTotal: verificar urls e arquivos maliciosos",
        'handler': virus_total
    }
}
