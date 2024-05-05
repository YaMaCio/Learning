import pymongo
import gridfs

def uploadDataAsFile(data, fileName, fs):
    fs.put(data, filename=fileName)
    
def findFileIdInDB(db, fs, fileName):
    data = db.files.files.find_one({"filename": fileName})
    return data['_id']