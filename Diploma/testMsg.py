import sys
import socket
import CoordsAndDb
import FirstMessage
from ctypes import *

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 9999  # The port used by the server
firstMessageSize = sys.getsizeof(FirstMessage)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        firstMessage = FirstMessage()
        msgBA = c_ubyte * (firstMessageSize + 8)
        msgPointer = POINTER(c_ubyte) 
        for i in 
        for j in range(firstMessageSize, firstMessageSize + 7):
            msgBA[j] = "#"
        s.sendall(b"Hello, world")
        
        print(f"Received {data!r}")