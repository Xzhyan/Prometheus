

class YtDownloader:
    def __init__(self):
        self.entry()

    def entry(self):
        cmd = input(" > ")


if __name__ == '__main__':
    try:
        YtDownloader()

    except KeyboardInterrupt:
        print("exiting")