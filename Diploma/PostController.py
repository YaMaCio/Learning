import pickle
import Post
from pymongo import * #MongoClient
import json
from bson import json_util
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
        tmpMsg1 = self.coll1.find_one({"mp1ID": id}, sort=[("_id", -1)])
        tmpMsg2 = self.coll1.find_one({"mp2ID": id}, sort=[("_id", -1)])
        tmpMsg3 = self.coll1.find_one({"mp3ID": id}, sort=[("_id", -1)])
        tmpMsg4 = self.coll2.find_one({"mp4ID": id}, sort=[("_id", -1)])
        if tmpMsg1 != None:
            return {
            "mpString": "mp1ID",
            "timestamp": tmpMsg1["timestamp"],
            "mpX": tmpMsg1["mp1CAndDb"]["x"],
            "mpY": tmpMsg1["mp1CAndDb"]["y"],
            "mpDb": tmpMsg1["mp1CAndDb"]["db"]
            }
        elif tmpMsg2 != None:
            return {
            "mpString": "mp2ID",
            "timestamp": tmpMsg2["timestamp"],
            "mpX": tmpMsg2["mp2CAndDb"]["x"],
            "mpY": tmpMsg2["mp2CAndDb"]["y"],
            "mpDb": tmpMsg2["mp2CAndDb"]["db"]
            }
        elif tmpMsg3 != None:
            return {
            "mpString": "mp3ID",
            "timestamp": tmpMsg3["timestamp"],
            "mpX": tmpMsg3["mp3CAndDb"]["x"],
            "mpY": tmpMsg3["mp3CAndDb"]["y"],
            "mpDb": tmpMsg3["mp3CAndDb"]["db"]
            }
        elif tmpMsg4 != None:
            return {
            "mpString": "mp4ID",
            "timestamp": tmpMsg4["timestamp"],
            "mpX": tmpMsg4["mp4CAndDb"]["x"],
            "mpY": tmpMsg4["mp4CAndDb"]["y"],
            "mpDb": tmpMsg4["mp4CAndDb"]["db"],
            "audioID": tmpMsg4["audioID"]
            }
        
    def calculateLatitudeAndLongitude(self, firstVertex, secondVertex, thirdVertex):
        r1 = self._coefficientOne * firstVertex["mpDb"]
        r2 = self._coefficientOne * secondVertex["mpDb"]
        r3 = self._coefficientOne * thirdVertex["mpDb"]
        
    def triangleToPost(self, triangle):
        firstVertex = self.findVertexByID(int(triangle._firstVertex))
        secondVertex = self.findVertexByID(int(triangle._secondVertex))
        thirdVertex = self.findVertexByID(int(triangle._thirdVertex))
        tmpPost = self.coll3.find_one({}, sort=[('_id', -1)])
        postID = None
        if tmpPost: 
            postID = tmpPost["_postID"] + 1
        else:
            postID = 1
        timestamp = firstVertex["timestamp"]
        triangleID = int(triangle._triangleID)
        latitude = 1
        longitude = 1
        address = "test"
        audioID = None
        if firstVertex["mpString"] == "mp4ID":
            audioID = firstVertex["audioID"]
        elif secondVertex["mpString"] == "mp4ID":
            audioID = secondVertex["audioID"]
        elif thirdVertex["mpString"] == "mp4ID":
            audioID = thirdVertex["audioID"]
        tmpRetPost = Post.Post(postID, timestamp, triangleID, latitude, longitude, address, audioID)
        tmp = self.coll3.insert_one(json.loads(json_util.dumps(vars(tmpRetPost))))
        return tmpRetPost
        
    def calculateTriangles(self, triangles):
        for triangle in triangles:
            self._posts.append(self.triangleToPost(triangle))
        
    def getPosts(self):
        tmp = self._posts
        return tmp
