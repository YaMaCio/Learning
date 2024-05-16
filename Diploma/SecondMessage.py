from ctypes import *
from CoordsAndDb import CAD

#class SecondMessage(Structure):
#    _fields_ = [("esp32id", c_int),
#                ("mp4id", c_int),
#                ("mp4canddb", CAD),
#                ("audio", c_ubyte * 8192)]

class SecondMessage(object):
    def __init__(self, esp32id, mp4id, mp4canddb, audio):
        self._esp32id      = esp32id
        self._mp4id     = mp4id
        self._mp4canddb    = mp4canddb
        self._audio = []
        for i in range(0, 8192-1):
            self._audio[i] = audio[i]