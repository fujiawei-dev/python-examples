import socket

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(b'get', ('localhost', 6688))
