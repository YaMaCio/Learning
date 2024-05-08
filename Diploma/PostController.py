import pickle
import Post
from pymongo import MongoClient

class PostController(object):

    def __init__(self):
        self._posts = []
        self._coefficientOne = 1
        self._coefficientTwo = 1
        self._coefficientThree = 1
        self.myclient = MongoClient("mongodb+srv://vitaliyskromyda:test@clusterdb.4wu0t0a.mongodb.net/?retryWrites=true&w=majority&appName=clusterdb", port=27017)
        self.mydb = myclient["clusterdb"]
        #fs = gridfs.GridFS(mydb, collection="files")
        self.coll1 = mydb["firstmsg"]
        self.coll2 = mydb["secondmsg"]
        self.coll3 = mydb["post"]

    def addPost(self, post):
        self._posts.append(post)

    def removePost(self, index):
        return self._posts.pop(index)

    def save(self, filename):
        output = open(filename, 'wb')
        pickle.dump(self._posts, output)

    def load(self, filename):
        pkl_file = open(filename, 'rb')
        self._posts = pickle.load(pkl_file)
        
    def findVertexByID(self, id):
        tmpMsg = None
        if tmpMsg = self.coll1.find_one({"mp1id": str(id)}, sort=[("_id", -1)]):
            return {
            "mpString" = "mp1id",
            "timestamp" = tmpMsg["timestamp"],
            "mpX": tmpMsg["mp1x"],
            "mpY": tmpMsg["mp1y"],
            "mpDb": tmpMsg["mp1Db"]
            }
        elif tmpMsg = self.coll1.find_one({"mp2id": str(id)}, sort=[("_id", -1)]):
            return {
            "mpString" = "mp2id",
            "timestamp" = tmpMsg["timestamp"],
            "mpX": tmpMsg["mp2x"],
            "mpY": tmpMsg["mp2y"],
            "mpDb": tmpMsg["mp2Db"]
            }
        elif tmpMsg = self.coll1.find_one({"mp3id": str(id)}, sort=[("_id", -1)]):
            return {
            "mpString" = "mp3id",
            "timestamp" = tmpMsg["timestamp"],
            "mpX": tmpMsg["mp3x"],
            "mpY": tmpMsg["mp3y"],
            "mpDb": tmpMsg["mp3Db"]
            }
        elif tmpMsg = self.coll2.find_one({"mp4id": str(id)}, sort=[("_id", -1)]):
            return {
            "mpString" = "mp4id",
            "timestamp" = tmpMsg["timestamp"],
            "mpX": tmpMsg["mp4x"],
            "mpY": tmpMsg["mp4y"],
            "mpDb": tmpMsg["mp4Db"],
            "audioID": tmpMsg["audioID"]
            }
        
    def calculateLatitudeAndLongitude(self, firstVertex, secondVertex, thirdVertex):
        r1 = self._coefficientOne * firstVertex["mpDb"]
        r2 = self._coefficientOne * secondVertex["mpDb"]
        r3 = self._coefficientOne * thirdVertex["mpDb"]
        
    def triangleToPost(self, triangle):
        firstVertex = self.findVertexByID(triangle._firstVertex)
        secondVertex = self.findVertexByID(triangle._secondVertex)
        thirdVertex = self.findVertexByID(triangle._thirdVertex)
        tmpPost = coll3.find_one({}, sort=[('_id', -1)])
        postID = None
        if tmpPost: 
            postID = tmpPost
        else:
            postID = 1
        timestamp = firstVertex["timestamp"]
        triangleID = triangle._triangleID
        latitude = 1
        longitude = 1
        address = "test"
        audioID = None
        if firstVertex["mpString"] == "mp4id"
            audioID = firstVertex["audioID"]
        elif secondVertex["mpString"] == "mp4id"
            audioID = secondVertex["audioID"]
        elif thirdVertex["mpString"] == "mp4id"
            audioID = thirdVertex["audioID"]
        return Post(postID, timestamp, triangleID, latitude, longitude, address, audioID)
        
    def calculateTriangles(self, triangles):
        for triangle in triangles:
            self._posts.append(triangleToPost(triangle))
        
    def getPosts(self):
        tmp = self._posts
        self._posts.clear()
        return tmp