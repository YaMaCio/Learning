import sys
from ctypes import *
import cCoordsAndDb
import cFirstMessage
import cSecondMessage
import logging

class MsgParser():
    def __init__(self):
        self._msg = None
        self._tmp = []
        self._res = None
        self._audio = (c_ubyte * 8192)()
        cdll.LoadLibrary("./cppForServer.dll")
        self._libCPP = CDLL("./cppForServer.dll")
        logging.info("Library loaded")
        self._libCPP.ByteArrayToFirstMessage.restype = cFirstMessage.cFirstMessage
        self._libCPP.FirstMessageCString.restype = c_char_p
        self._libCPP.ByteArrayToSecondMessage.restype = cSecondMessage.cSecondMessage
        self._libCPP.SecondMessageCString.restype = c_char_p
        self._libCPP.ExtractAudioFromSecondMessage.restype = None
        logging.info("Results type set")
        self._libCPP.ByteArrayToFirstMessage.argtypes = [c_void_p]
        self._libCPP.FirstMessageCString.argtypes = [POINTER(cFirstMessage.cFirstMessage)]
        self._libCPP.ByteArrayToSecondMessage.argtypes = [c_void_p]
        self._libCPP.SecondMessageCString.argtypes = [POINTER(cSecondMessage.cSecondMessage)]
        self._libCPP.ExtractAudioFromSecondMessage.argtypes = [POINTER(cSecondMessage.cSecondMessage), c_void_p]
        logging.info("Library set")

    def setMessage(self, msg):
        self._msg = msg
        
    def parsing(self):
        specialSymNum = 0
        endFlag = False
        logging.info("Parsing started")
        iter = 0
        k = 0

        for i in self._msg:
            logging.info("Iteration: " + str(iter))
            self._tmp.append(i)
            if len(self._tmp) > 8:
                for j in range(len(self._tmp)-8, len(self._tmp)):
                    if self._tmp[j] == 35:
                        specialSymNum += 1
                if specialSymNum != 8:
                    logging.info("Special symbols: " + str(specialSymNum))
                    specialSymNum = 0
            if specialSymNum == 8:
                logging.info("Special symbols: " + str(specialSymNum))
                endFlag = True
                for k in range(8):
                    logging.info("Popping array")
                    self._tmp.pop()
                    logging.info(str(k))
                if k == 7:
                    iter -= 8
            logging.info(str(self._tmp[iter]))
            iter += 1
            if endFlag == True:    
                break

        iter = 0
        logging.info(str(len(self._tmp)))
        logging.info("Creating array")
        cTypeArray = (c_ubyte * len(self._tmp))()

        logging.info("Copying array")
        for m in range(0, len(self._tmp)):
            logging.info("Iteration: " + str(m))
            cTypeArray[m] = self._tmp[m]
            logging.info(str(cTypeArray[m]))
        logging.info("Array copied")
        if len(cTypeArray) < 8212:
            logging.info("Creating first message JSON")
            firstMsg = self._libCPP.ByteArrayToFirstMessage(cTypeArray)
            tmpChar = self._libCPP.FirstMessageCString(pointer(firstMsg))
            self._res = tmpChar.decode()
            logging.info("JSON created")
            self._size = 52
        else:
            logging.info("Creating second message JSON")
            secondMsg = self._libCPP.ByteArrayToSecondMessage(cTypeArray)
            tmpChar = self._libCPP.SecondMessageCString(pointer(secondMsg))
            self._res = tmpChar.decode()
            logging.info("JSON created")
            self._libCPP.ExtractAudioFromSecondMessage(pointer(secondMsg), self._audio)
            logging.info("Audio extracted")
            self._size = 8212
        
    def getSize(self):
        return self._size
    
    def getTempMessage(self):
        return self._tmp
    
    def getJSONString(self):
        return self._res
        
    def getAudio(self, audioArray):
        for l in range(0, 8192):
            audioArray.append(self._audio[l])