from ctypes import *
import CoordsAndDb

class FirstMessage(Structure):
    _fields_ = [("esp32id", c_int),
                ("mp1id", c_int),
                ("mp1canddb", CoordsAndDb),
                ("mp2id", c_int),
                ("mp2canddb", CoordsAndDb),
                ("mp3id", c_int),
                ("mp3canddb", CoordsAndDb)]