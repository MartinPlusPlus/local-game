import socket
import sys
import random

random.seed()

HOST = "192.168.0.110" # Temporary
PORT = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.getaddrinfo(HOST, PORT, socket.AF_INET, socket.SOCK_STREAM))
s.connect((HOST, 5050))

cool_num = bytes([random.randrange(48, 58)])

s.sendall(cool_num)
