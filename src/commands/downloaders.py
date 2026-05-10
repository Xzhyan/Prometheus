

def yt_dlp():
    pass


DOWNLOADERS_COMMANDS = {
    'yt': {
        'func': lambda: yt_dlp(),
        'desc': "Baxiar vídeos e músicas do YouTube",
        'usage': "type [yt help] to show help menu"
    },
}
