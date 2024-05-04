import pickle

class TriangleController(object):

    def __init__(self):
        self._triangles = []

    def addTriangle(self, triangle):
        self._triangles.append(triangle)

    def removeTriangle(self, index):
        return self._triangles.pop(index)

    def save(self, filename):
        output = open(filename, 'wb')
        pickle.dump(self._triangles, output)

    def load(self, filename):
        pkl_file = open(filename, 'rb')
        self._triangles = pickle.load(pkl_file)