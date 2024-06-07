import functools
import socket
import sys
from pymongo import *
import gridfs
from time import gmtime, strftime, time
from ctypes import *
from MsgParser import MsgParser
import json
import DBFunctions
import asyncio
import logging
import signal



def ask_exit(signame, loop):
     print("got signal %s: exit" % signame)
     loop.stop()
async def handle_client(reader, writer):
    logging.info("Client connected")
    addr = writer.get_extra_info('peername')
    msgParser = MsgParser()
    dataBuffer = bytearray()
    logging.info("Start reading")
    data = await reader.read(16384)
    dataBuffer.extend(data)
    cUByteArray = (c_ubyte * len(dataBuffer)).from_buffer_copy(dataBuffer)
    msgParser.setMessage(cUByteArray)
    testIter = 0
    for i in cUByteArray:
        logging.info(str(testIter) + " " + str(i))
        testIter += 1
    logging.info("Data parsing")
    msgParser.parsing()
    logging.info("Converting data...")
    if msgParser.getSize() < 8212:
        logging.info("Creating timestamp")
        timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        logging.info("Parsing JSON")
        tmpdict = json.loads(msgParser.getJSONString())
        tmpdict['timestamp'] = timestamp
        logging.info("Data formated")
        tmp = coll1.insert_one(tmpdict)
        logging.info("Data added to DB")
    else:
        logging.info("Creating timestamp")
        timeInSec = time() - 5
        timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime(timeInSec))
        audio = []
        logging.info("Extracting audio")
        msgParser.getAudio(audio)
        logging.info("Uploading audio")
        DBFunctions.uploadDataAsFile(audio, fs, timestamp + ".mp3")
        logging.info("Finding audio ID")
        fileID = DBFunctions.findFileIdInDB(mydb, fs, timestamp + ".mp3")
        logging.info("Parsing JSON")
        tmpdict = json.loads(msgParser.getJSONString())
        tmpdict['timestamp'] = timestamp
        tmpdict['audioID'] = fileID
        logging.info("Data formated")
        tmp = coll2.insert_one(tmpdict)
        logging.info("Data added to DB")
    writer.close()

async def runServer():
    logging.info("Entered in runServer()")
    server = await asyncio.start_server(handle_client, host, port)
    logging.info("Server created")
    await server.serve_forever()


        
if __name__ == '__main__':
    global host, port, myclient, mydb, fs, coll1, coll2
    host = "127.0.0.1"
    port = 9876
    myclient = MongoClient(
        "mongodb+srv://vitaliyskromyda:test@clusterdb.4wu0t0a.mongodb.net/?retryWrites=true&w=majority&appName=clusterdb",
        port=27017)
    mydb = myclient["clusterdb"]
    fs = gridfs.GridFS(mydb, collection="files")
    coll1 = mydb["firstmsg"]
    coll2 = mydb["secondmsg"]
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    logging.basicConfig(level=logging.DEBUG, filename="TCPServer.log", filemode="w"
                        , format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info("Starting TCPServer")
    asyncio.run(runServer(), debug = True)
    logging.info("TCPServer started")