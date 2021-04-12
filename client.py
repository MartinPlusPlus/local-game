import socket
import sys

HOST = "localhost" # Temporary
PORT = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.getaddrinfo(HOST, PORT, socket.AF_INET, socket.SOCK_STREAM))
s.connect(("127.0.0.1", 5050))

s.sendall(b"Hello, World!")
