import sys
import socket
import time
import cCoordsAndDb
import cFirstMessage
import cSecondMessage
from ctypes import *

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 9999  # The port used by the server
firstMessageSize = 52
secondMessageSize = 8212
cdll.LoadLibrary("./cppWinForServer.so")
libcpp = CDLL("./cppWinForServer.so")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        firstMessage = libcpp.getFirstMessageInstance()
        firstMsgBA = c_ubyte * (firstMessageSize + 8)
        firstMsgPointer = pointer(firstMessage)
        #firstMsgPointer = cast(firstMsgPointer, POINTER(c_ubyte))
        libcpp.FirstMessageToByteArray(firstMsgPointer, firstMsgBA)
        #for i in range(0, firstMessageSize - 1):
        #    firstMsgBA[i] = (firstMsgPointer + i).contents
        for j in range(firstMessageSize, firstMessageSize + 7):
            firstMsgBA[j] = "#"
        s.send(firstMsgBA)
        
        sleep(5)
        
        secondMessage = libcpp.getSecondMessageInstance()
        secondMsgBA = c_ubyte * (secondMessageSize + 8)
        secondMsgPointer = pointer(secondMessage)
        #secondMsgPointer = cast(secondMsgPointer, POINTER(c_ubyte))
        libcpp.SecondMessageToByteArray(secondMsgPointer, secondMsgBA)
        #for i in range(0, firstMessageSize - 1):
        #    secondMsgBA[i] = (secondMsgPointer + i).contents
        for j in range(secondMessageSize, secondMessageSize + 7):
            secondMsgBA[j] = "#"
        s.send(secondMsgBA)