import socket

services = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

target = input("Enter IP or hostname: ")
print(f"\nScanning {target}...\n")

open_ports = []

for port in services:
    s = socket.socket()
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        open_ports.append(port)
        print(f"[OPEN] Port {port}: {services[port]}")

    s.close()

print("\nScan Complete!")
print(f"Open ports: {open_ports}")