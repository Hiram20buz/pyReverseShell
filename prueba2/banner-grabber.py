# !/usr/bin/python
#python2.7
import socket


def grab_banner(ip_address, port):
    try:
        s = socket.socket()
        s.connect((ip_address, port))
        banner = s.recv(1024)
        s.close()
        return banner
    except:
        return ''


def main():
    ports = [2323]
    for port in ports:
        ip_address = '192.168.0.2'
        print grab_banner(ip_address, port)


if __name__ == '__main__':
    main()
