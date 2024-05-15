from ctypes import *
from CoordsAndDb import CAD

#class FirstMessage(Structure):
#    _fields_ = [("esp32id", c_int),
#                ("mp1id", c_int),
#                ("mp1canddb", CAD),
#                ("mp2id", c_int),
#                ("mp2canddb", CAD),
#                ("mp3id", c_int),
#                ("mp3canddb", CAD)]

class FirstMessage(object):
    def __init__(self, esp32id, mp1id, mp1canddb, mp2id, mp2canddb, mp3id, mp3canddb):
        self._esp32id      = esp32id
        self._mp1id     = mp1id
        self._mp1canddb    = mp1canddb
        self._mp2id     = mp2id
        self._mp2canddb    = mp2canddb
        self._mp3id     = mp3id
        self._mp3canddb    = mp3canddb