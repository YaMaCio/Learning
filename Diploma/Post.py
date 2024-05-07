class Post(object):

    def __init__(self, timestamp, triangleID, latitude, longitude, address, audioID):
        self._timestamp       = timestamp
        self._triangleID      = triangleID
        self._latitude        = latitude
        self._longitude       = longitude
        self._address         = address
        self._audioID         = audioID
