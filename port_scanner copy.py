import socket
import threading
services={20:"FTP Data",
          21:"FTP",
          22:"SSH",
          23:"Telnet",
          53:"DNS",
          80:"HTTP",
          110:"POP3",
          143:"IMAP",
          443:"HTTPS"}

target=input("Enter IP or hostname:")
print(f"\nScanning {target}...\n")

open_ports=[]
lock= threading.Lock()

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)

            if s.connect_ex((target,port))==0:
                service=services.get(port,"Unknown")
                with lock:
                    open_ports.append(port)
                    print(f"[OPEN] Port:{port}:{service}")
    
    except:
        pass

threads=[]

for port in range(1,1001):
    t=threading.Thread(target=scan_port,args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nScan Complete!")
print(f"open ports={sorted(open_ports)}")
