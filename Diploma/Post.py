class Post(object):

    def __init__(self, postID, timestamp, triangleID, latitude, longitude, address, audioID):
        self._postID          = postID
        self._timestamp       = timestamp
        self._triangleID      = triangleID
        self._latitude        = latitude
        self._longitude       = longitude
        self._address         = address
        self._audioID         = audioID
