from ctypes import *
from CoordsAndDb import CAD

class FirstMessage(Structure):
    _fields_ = [("esp32id", c_int),
                ("mp4id", c_int),
                ("mp4canddb", CAD),
                ("audio", c_ubyte * 8192)]