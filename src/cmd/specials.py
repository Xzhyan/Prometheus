import yt_dlp

# core
from core import settings
from core.logger import addlog
from core.constants import FFMPEG_DIR, OUTPUT_DIR

# core/exceptions
from core.exceptions import ArgumentError

# utils/system
from utils.system import run_python_module


def easy_sharing(*args):
    run_python_module(
        settings.EASY_PATH,
        'manage.py',
        'runserver',
        settings.EASY_SERVER_IP
    )


class YoutubeDownloader:
    def __init__(self, args):
        cmd = args[1] # comando 'music/video'
        url = args[2] # url do yt

        if not cmd:
            addlog('error', f"ARGUMENT_ERROR | argumento inválido")
            raise ArgumentError("exemplo de uso: yt music/video")

        if not url:
            addlog('error', f"URL_ERROR | url inválida")
            raise ArgumentError("você precisa informar uma url válida")
        
        self.dispatch(cmd, url)

    def download_music(self, url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'ffmpeg_location': FFMPEG_DIR,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl': f'{OUTPUT_DIR}\\%(title)s.%(ext)s',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        except Exception as e:
            addlog('error', str(e))
            print(str(e))


    def dispatch(self, cmd, url):
        if cmd == 'music':
            try:
                self.download_music(url)
            
            except Exception as e:
                print(e)

        else:
            raise ValueError("o tipo não existe")


SPECIAL_COMMANDS = {
    'easy': {
        'desc': "inicia o EasySharing (ftp/drive local)",
        'handler': easy_sharing
    },
    'yt': {
        'desc': "faz download de conteúdos do YouTube",
        'handler': lambda args: YoutubeDownloader(args)
    }
}
