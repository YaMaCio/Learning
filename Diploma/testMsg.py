import sys
import socket
import time
import cCoordsAndDb
import cFirstMessage
import cSecondMessage
from ctypes import *
import logging

logging.basicConfig(level=logging.DEBUG, filename="testMsg.log", filemode="w"
                        , format="%(asctime)s - %(levelname)s - %(message)s")
HOST = "127.0.0.1"#"91.200.201.167" #socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address
PORT = 9876  # The port used by the server
firstMessageSize = 52
secondMessageSize = 8212
cdll.LoadLibrary("./cppForServer.dll")
libcpp = CDLL("./cppForServer.dll")
libcpp.getFirstMessageInstance.restype = cFirstMessage.cFirstMessage
libcpp.getSecondMessageInstance.restype = cSecondMessage.cSecondMessage
libcpp.FirstMessageToByteArray.argtypes = [POINTER(cFirstMessage.cFirstMessage), c_void_p]
libcpp.SecondMessageToByteArray.argtypes = [POINTER(cSecondMessage.cSecondMessage), c_void_p]
logging.info("DLL attached")
hashTag = c_ubyte(35) # sign '#'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    logging.info("Socket created")
    s.connect((HOST, PORT))
    logging.info("Socket connected")
    for i in range(1):
        #logging.info("Creating first message")
        #firstMessage = libcpp.getFirstMessageInstance()
        #firstMsgBA = (c_ubyte * (firstMessageSize + 8))()
        #firstMsgPointer = pointer(firstMessage)
        ##firstMsgPointer = cast(firstMsgPointer, POINTER(c_ubyte))
        #libcpp.FirstMessageToByteArray(firstMsgPointer, cast(firstMsgBA, c_void_p))
        ##for i in range(0, firstMessageSize - 1):
        ##    firstMsgBA[i] = (firstMsgPointer + i).contents
        #for j in range(firstMessageSize, firstMessageSize + 8):
        #    firstMsgBA[j] = hashTag
        #logging.info("First message was formated")
        #s.send(firstMsgBA)
        #logging.info("First message was sent")
        
        #time.sleep(5)

        logging.info("Creating second message")
        secondMessage = libcpp.getSecondMessageInstance()
        secondMsgBA = (c_ubyte * (secondMessageSize + 8))()
        secondMsgPointer = pointer(secondMessage)
        #secondMsgPointer = cast(secondMsgPointer, POINTER(c_ubyte))
        libcpp.SecondMessageToByteArray(secondMsgPointer, cast(secondMsgBA, c_void_p))
        #for i in range(0, firstMessageSize - 1):
        #    secondMsgBA[i] = (secondMsgPointer + i).contents
        for j in range(secondMessageSize, secondMessageSize + 8):
            secondMsgBA[j] = hashTag
        logging.info("Second message was formated")
        s.send(secondMsgBA)
        logging.info("Second message was sent")