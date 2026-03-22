import socket
def scan(target):
    open_ports = []
    print("[*] Scanning ports...")

    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)

        result = sock.connect_ex((target, port))
        if result == 0:
            print(f'[+] Open port: {port}')
            open_ports.append(port)

        sock.close()

    return open_ports
