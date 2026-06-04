import socket


def tcp_scan(host):
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)

        print(f'testando porta: {port}')
        
        if sock.connect_ex((host, port)) == 0:
            print(f'Porta aberta: {port}')

        sock.close()



class Main:
    def __init__(self):
        self.running = True

    def startup(self):
        self.dispatch()

    def dispatch(self):
        while self.running:
            try:
                tcp_scan('172.25.188.127')

            except Exception as e:
                print(str(e))

if __name__ == '__main__':
    try:
        portscan = Main()
        portscan.startup()

    except KeyboardInterrupt:
        print("Saindo...")