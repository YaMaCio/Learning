import sys
from ctypes import *
import cFirstMessage
import cSecondMessage

class MsgParser():
    def __init__(self):
        self._msg = None
        self._tmp = []
        self._res = None
        self._audio = c_ubyte * 8192
        cdll.LoadLibrary("./cppForServer.dll")
        self._libcpp = CDLL("./cppForServer.dll") 
        
    def setMessage(self, msg):
        self._msg = msg
        
    def parsing(self):
        specialSymNum = 0
        endFlag = False
        
        for i in self._msg:
            self._tmp.append(i)
            if len(self._tmp) > 8:
                for j in range(len(self._tmp)-8, len(self._tmp)):
                    if self._tmp[j] == '#':
                        specialSymNum += 1
                if specialSymNum != 8:
                    specialSymNum = 0
            if specialSymNum == 8:
                endFlag = True
                for k in range(8):
                    self._tmp.pop()
            if endFlag == True:    
                break
                
        cTypeArray = c_ubyte * len(self._tmp)
        
        for i in range(0, len(self._tmp)-1):
            cTypeArray[i] = self._tmp[i]
        if len(cTypeArray) < 8212:
            self._res = self._libcpp.FirstMessageCString(pointer(self._libcpp.ByteArrayToFirstMessage(cTypeArray))).value
            self._size = 52
        else:
            self._res = self._libcpp.SecondMessageCString(pointer(self._libcpp.ByteArrayToSecondMessage(cTypeArray))).value
            self._libcpp.ExtractAudioFromSecondMessage(pointer(self._libcpp.ByteArrayToSecondMessage(cTypeArray)), self._audio)
            self._size = 8212
        
    def getSize(self):
        return self._size
    
    def getTempMessage(self):
        return self._tmp
    
    def getJSONString(self):
        return self._res
        
    def getAudio(self, audioArray):
        for i in range(0, 8192-1):
            audioArray[i] = self._audio[i]