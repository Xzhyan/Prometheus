# core
from core import settings

# scapy
from scapy.all import sniff, TCP, IP


def tcp_capture(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        if packet[TCP].flags == 'S':
            print(f'SYN | {packet[IP].src}  -> {packet[IP].dst}')




class IntrusionDetectionSystem:
    def __init__(self):
        pass

    def startup(self):
        sniff(filter='tcp', prn=tcp_capture, store=False)



if __name__ == '__main__':
    try:
        main = IntrusionDetectionSystem()
        main.startup()
    
    except KeyboardInterrupt:
        print('Finalizando...')
