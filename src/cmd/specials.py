import yt_dlp

# core
from core import settings
from core.constants import FFMPEG_DIR, OUTPUT_DIR

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
        op_type = args[1]
        url_link = args[2]

        if not op_type or not url_link:
            raise ValueError("faltou argumento")
        
        self.dispatch(op_type, url_link)

    def download_music(self, url_link):
        ydl_opts = {
            'format': 'bestaudio/best',
            'ffmpeg_location': FFMPEG_DIR,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{OUTPUT_DIR}\\%(title)s.%(ext)s',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url_link])

        except Exception as e:
            print(e)


    def dispatch(self, op_type, url_link):
        if op_type == 'music':
            try:
                self.download_music(url_link)
            
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
