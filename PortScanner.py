import socket
from IPy import IP

from vulnScanner import targets


class PortScan():
    banners=[]
    open_ports=[]
    def __init__(self,target,port_num):
        self.target=targets_ip
        self.port_num=port_num
    def scan(self):
        #converted_id=check_ip(target)
        #print('\n' + "[-_0 Scanning Target]"+str(target))
        for port in range(1,500):
            self.scan_port(port)

    def check_ip(self):
        try:
            IP(self.target)
            return (self.target)
        except ValueError:
            return socket.gethostbyname(ip)

    def get_banner(s):
        return.recv(1024)
    def scan_prt(selfself,port):
        try:
            converted_ip=self.check_ip()
            sock=socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip,port))
            self.open_ports.append(port)
            try:
                banner=sock.recv(1024).decode().strip('\n').strip('\r')
                self.banenrs.append(banner)
            except:
                self.banners.append(' ')
            sock.close()
        except:
            pass