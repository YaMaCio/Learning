from ctypes import *
from CoordsAndDb import CAD

class FirstMessage(Structure):
    _fields_ = [("esp32id", c_int),
                ("mp1id", c_int),
                ("mp1canddb", CAD),
                ("mp2id", c_int),
                ("mp2canddb", CAD),
                ("mp3id", c_int),
                ("mp3canddb", CAD)]