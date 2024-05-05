import sys
from ctypes import *
import FirstMessage
import SecondMessage

class MsgParser():
    def __init__(self):
        self._msg = None
        self._tmp = []
        self._res = None
        
    def setMsg(self, msg):
        self._msg = msg
        
    def parsing(self):
        specialSymNum = 0
        for i in self._msg:
            self._tmp.append(i)
            if len(self._tmp) > 8:
                for j in range(len(self._tmp)-8, len(self._tmp)):
                    if self._tmp[j] == '#':
                        specialSymNum += 1
                if specialSymNum != 8:
                    specialSymNum = 0
            if specialSymNum == 8:
                if k in range(8):
                    self._tmp.pop()
                break
        cTypeArray = c_char * len(self._tmp)
        for i in range(0, len(self._tmp)-1)
            cTypeArray[i] = self._tmp[i]
        if sys.getsizeof(cTypeArray) < sys.getsizeof(SecondMessage):
            self._res = cast(cTypeArray, FirstMessage)
        else:
            self._res = cast(cTypeArray, SecondMessage)
        
    def getMsg(self):
        return self._res