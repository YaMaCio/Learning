import pickle
import Post
from pymongo import MongoClient
#import pymongo

class PostController(object):

    def __init__(self):
        self._posts = []
        self._coefficientOne = 1
        self._coefficientTwo = 1
        self._coefficientThree = 1
        self.myclient = MongoClient("mongodb+srv://vitaliyskromyda:test@clusterdb.4wu0t0a.mongodb.net/?retryWrites=true&w=majority&appName=clusterdb", port=27017)
        self.mydb = self.myclient["clusterdb"]
        #fs = gridfs.GridFS(mydb, collection="files")
        self.coll1 = self.mydb["firstmsg"]
        self.coll2 = self.mydb["secondmsg"]
        self.coll3 = self.mydb["post"]

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
        tmpMsg1 = self.coll1.find_one({"mp1id": str(id)}, sort=[("_id", -1)])
        tmpMsg2 = self.coll1.find_one({"mp2id": str(id)}, sort=[("_id", -1)])
        tmpMsg3 = self.coll1.find_one({"mp3id": str(id)}, sort=[("_id", -1)])
        tmpMsg4 = self.coll2.find_one({"mp4id": str(id)}, sort=[("_id", -1)])
        if tmpMsg1:
            return {
            "mpString": "mp1id",
            "timestamp": tmpMsg1["timestamp"],
            "mpX": tmpMsg1["mp1x"],
            "mpY": tmpMsg1["mp1y"],
            "mpDb": tmpMsg1["mp1Db"]
            }
        elif tmpMsg2:
            return {
            "mpString": "mp2id",
            "timestamp": tmpMsg2["timestamp"],
            "mpX": tmpMsg2["mp2x"],
            "mpY": tmpMsg2["mp2y"],
            "mpDb": tmpMsg2["mp2Db"]
            }
        elif tmpMsg3:
            return {
            "mpString": "mp3id",
            "timestamp": tmpMsg3["timestamp"],
            "mpX": tmpMsg3["mp3x"],
            "mpY": tmpMsg3["mp3y"],
            "mpDb": tmpMsg3["mp3Db"]
            }
        elif tmpMsg4:
            return {
            "mpString": "mp4id",
            "timestamp": tmpMsg4["timestamp"],
            "mpX": tmpMsg4["mp4x"],
            "mpY": tmpMsg4["mp4y"],
            "mpDb": tmpMsg4["mp4Db"],
            "audioID": tmpMsg4["audioID"]
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
        if firstVertex["mpString"] == "mp4id":
            audioID = firstVertex["audioID"]
        elif secondVertex["mpString"] == "mp4id":
            audioID = secondVertex["audioID"]
        elif thirdVertex["mpString"] == "mp4id":
            audioID = thirdVertex["audioID"]
        return Post(postID, timestamp, triangleID, latitude, longitude, address, audioID)
        
    def calculateTriangles(self, triangles):
        for triangle in triangles:
            self._posts.append(triangleToPost(triangle))
        
    def getPosts(self):
        tmp = self._posts
        self._posts.clear()
        return tmp