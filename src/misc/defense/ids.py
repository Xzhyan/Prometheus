from scapy.all import sniff, TCP, IP


def tcp_capture(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        if packet[TCP].flags == 'S':
            print(f'SYN | {packet[IP].src} -> {packet[IP].dst}')


class IntrusionDefenseSystem:
    def __init__(self):
        pass

    def startup(self):
        sniff(filter='tcp', prn=tcp_capture, store=False)


if __name__ == '__main__':
    try:
        ids = IntrusionDefenseSystem()
        ids.startup()

    except KeyboardInterrupt:
        print("Saindo...")