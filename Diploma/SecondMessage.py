from ctypes import *
import CoordsAndDb

class FirstMessage(Structure):
    _fields_ = [("esp32id", c_int),
                ("mp4id", c_int),
                ("mp4canddb", CoordsAndDb),
                ("audio", c_char * 8192)]