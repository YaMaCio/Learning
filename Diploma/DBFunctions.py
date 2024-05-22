import pymongo
import gridfs

def uploadDataAsFile(data, fs, fileName):
    fs.put(bytearray(data), filename=fileName)
    
def findFileIdInDB(db, fs, fileName):
    data = db.files.files.find_one({"filename": fileName})
    return data['_id']