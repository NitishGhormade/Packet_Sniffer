import socket

def packet_sniffer():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    host = socket.gethostbyname(socket.gethostname())
    s.bind((host, 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    print("Listening for packets...")
    try:
        while True:
            packet, _ = s.recvfrom(65565)
            print(f"Packet: {packet}")
    except KeyboardInterrupt:
        print("\nStopping packet capture.")
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == "__main__":
    packet_sniffer()
