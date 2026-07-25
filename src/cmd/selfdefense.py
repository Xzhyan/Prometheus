import subprocess

# core
from core.config import settings

# ui
from ui.ui_console import alert


def open_url_link(url):
    """Abre o nevegador padrão no link fixado"""

    try:
        subprocess.Popen(f'start {url}', shell=True)

    except Exception as e:
        alert('error', str(e))


SELF_DEFENSE = {
    'link-checker': {
        'desc': "bitdefender: verificador de link malicioso",
        'handler': lambda url: open_url_link(settings.BIT_LINK_CHECKER_URL)
    },
    'virus-total': {
        'desc': "virustotal: verificar urls e arquivos maliciosos",
        'handler': lambda url: open_url_link(settings.VIRUS_TOTAL_URL)
    },
    'bitwarden': {
        'desc': "cofre e gerenciador de credenciais gratuito",
        'handler': lambda url: open_url_link(settings.BITWARDEN)
    },
    'protonvpn': {
        'desc': "aplicativo de VPN com acesso gratuito",
        'handler': lambda url: open_url_link(settings.PROTON_VPN)
    }
}

