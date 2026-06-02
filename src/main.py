from core import settings



class Main:
    def __init__(self):
        pass

    
    def startup(self):
        pass

    
    def dispatch(self):
        pass



if __name__ == '__main__':
    try:
        tool = Main()
        tool.startup()

    except KeyboardInterrupt:
        print('saindo...')
