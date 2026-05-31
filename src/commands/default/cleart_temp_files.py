import sys

from pathlib import Path


class Main:
    def __init__(self):
        pass

    def run(self):
        print("test")

    def dispatch(self):
        pass


if __name__ == '__main__':
    try:
        tool = Main()
        tool.run()

    except KeyboardInterrupt:
        print("")
        sys.exit()