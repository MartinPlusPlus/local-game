import socket
from _thread import *
import sys

HOST = ""
PORT = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("Server started")
print("Waiting for a connection to the server...")

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    # Start a new thread after this to process signals
    data = conn.recv(1024)
    data = data.decode("utf-8")
    print(data)
