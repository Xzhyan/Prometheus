from utils.console import run_subprocess


def yt_dlp():
    run_subprocess(r'src\commands\downloaders\yt_dlp.py')


DOWNLOADERS_COMMANDS = {
    'yt': {
        'func': lambda: yt_dlp(),
        'desc': "Baxiar vídeos e músicas do YouTube",
        'usage': "type [yt help] to show help menu"
    },
}
