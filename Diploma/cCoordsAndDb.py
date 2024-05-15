from ctypes import *

class cCAD(Structure):
    _fields_ = [("x", c_float),
                ("y", c_float),
                ("db", c_float)]

#class CAD(object):
#    def __init__(self, x, y, db):
#        self._x = x
#        self._y = y
#        self._db = db