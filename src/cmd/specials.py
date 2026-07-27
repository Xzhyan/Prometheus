import yt_dlp
import webview

# core
from core import settings
from core.logger import addlog
from core.constants import FFMPEG_DIR, OUTPUT_DIR, MONITOR_HTML

# ui
from ui.ui_console import alert

# core/exceptions
from core.exceptions import ArgumentError

# utils/system
from utils.system import run_python_module



class Monitor:
    def __init__(self, *args):
        self.window = None

    def create_window(self):
        self.window = webview.create_window(
            title="Monitor do sistema",
            url=MONITOR_HTML.as_uri(),
            width=400,
            height=300,
            x=0,
            y=30,
            transparent=True,
        )

    def start_window(self):
        self.create_window()
        webview.start(debug=False)


def sysinfo(*args):
    monitor = Monitor()
    monitor.start_window()


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
            'format': "bestaudio/best",
            'ffmpeg_location': FFMPEG_DIR,
            'postprocessors': [{
                'key': "FFmpegExtractAudio",
                'preferredcodec': "mp3",
                'preferredquality': "320",
            }],
            'outtmpl': f"{OUTPUT_DIR}\\%(title)s.%(ext)s",
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        except Exception as e:
            addlog('error', str(e))
            alert('error', str(e))

    def download_video(self, url):
        ydl_opts = {
            'format': "bestvideo+bestaudio/best",
            'outtmpl': f"{OUTPUT_DIR}\\%(title)s.%(ext)s",
            'merge_output_formart': "mp4"
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        
        except Exception as e:
            addlog('error', str(e))
            alert('error', str(e))

    def dispatch(self, cmd, url):
        if cmd == 'music':
            self.download_music(url)

        elif cmd == 'video':
            self.download_video(url)

        else:
            raise ValueError("os tipos aceitos são [music] e [video]")


SPECIAL_COMMANDS = {
    'easy': {
        'desc': "inicia o EasySharing (ftp/drive local)",
        'handler': easy_sharing
    },
    'yt': {
        'desc': "faz download de conteúdos do YouTube",
        'handler': lambda args: YoutubeDownloader(args)
    },
    # 'sysinfo': {
    #     'desc': "exibe informações do sistema",
    #     'handler': sysinfo
    # }
}
