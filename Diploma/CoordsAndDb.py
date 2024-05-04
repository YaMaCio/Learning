from ctypes import *

class CoordsAndDb(Structure):
    _fields_ = [("x", c_float),
                ("y", c_float),
                ("Db", c_float)]