import socket
def grab(target, ports):
    banners = {}
    print("[*] Grabbing banners...")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((target, port))
            banner = sock.recv(1024).decode(errors="ignore").strip()
            banners[port] = banner if banner else  "No banner"

            sock.close()
        except:
            banners[port] = "Unknown"

        print (f'[+] Port {port}: {banners[port]}')
    return banners