import socket
from pymongo import MongoClient
import gridfs
from time import gmtime, strftime
from ctypes import *
from MsgParser import MsgParser
import json
import DBFunctions
import asyncio

class TCPServer:
    async def handle_client(self, client):
        loop = asyncio.get_event_loop()
        request = None
        msgParser = MsgParser()
        while request != 'quit':
            request = (await loop.sock_recv(client, 16384))
            msgParser.setMessage(data)
            if sys.getsizeof(msgParser.getTempMessage()) < sys.getsizeof(cSecondMessage):
                timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                tmpdict = loads(msgParser.getJSONString())
                tmpdict['timestamp'] = timestamp
                tmp = coll1.insert_one(tmpdict)
            else:
                timeInSec = time() - 5
                timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime(timeInSec))
                uploadDataAsFile(msgParser.getMsg().audio, fs, timestamp + ".mp3")
                fileID = findFileInDB(mydb, fs, timestamp + ".mp3")
                tmpdict = loads(msgParser.getJSONString())
                tmpdict['audioID'] = fileID
                tmp = coll2.insert_one(tmpdict)
        client.close()

    async def runServer(self):
        # get the hostname
        host = socket.gethostname()
        port = 9999  # initiate port no above 1024
        myclient = MongoClient("mongodb+srv://vitaliyskromyda:test@clusterdb.4wu0t0a.mongodb.net/?retryWrites=true&w=majority&appName=clusterdb", port=27017)
        mydb = myclient["clusterdb"]
        fs = gridfs.GridFS(mydb, collection="files")
        coll1 = mydb["firstmsg"]
        coll2 = mydb["secondmsg"]

        server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        server_socket.listen(300)
        server_socket.setblocking(False)
        loop = asyncio.get_event_loop()
        #conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            conn, address = await loop.sock_accept(server_socket)
            loop.create_task(self.handle_client(client))
            # receive data stream. it won't accept data packet greater than 10240 bytes
            #data = conn.recv(16384)
            #msgParser.setMsg(data)
            #if sys.getsizeof(msgParser.getMsg()) < sys.getsizeof(SecondMessage):
            #    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            #    tmpdict = { 
            #    "timestamp": timestamp, 
            #    "esp32id": str(msgParser.getMsg().esp32id),
            #    "mp1id": str(msgParser.getMsg().mp1id),
            #    "mp1x": str(msgParser.getMsg().mp1canddb.x),
            #    "mp1y": str(msgParser.getMsg().mp1canddb.y),
            #    "mp1db": str(msgParser.getMsg().mp1canddb.db),
            #    "mp2id": str(msgParser.getMsg().mp2id),
            #    "mp2x": str(msgParser.getMsg().mp2canddb.x),
            #    "mp2y": str(msgParser.getMsg().mp2canddb.y),
            #    "mp2db": str(msgParser.getMsg().mp2canddb.db),
            #    "mp3id": str(msgParser.getMsg().mp3id),
            #    "mp3x": str(msgParser.getMsg().mp3canddb.x),
            #    "mp3y": str(msgParser.getMsg().mp3canddb.y),
            #    "mp3db": str(msgParser.getMsg().mp3canddb.db)}
            #    tmp = coll1.insert_one(tmpdict)
            #else:
            #    timeInSec = time() - 5
            #    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime(timeInSec))
            #    uploadDataAsFile(msgParser.getMsg().audio, fs, timestamp + ".mp3")
            #    fileId = findFileInDB(mydb, fs, timestamp + ".mp3")
            #    tmpdict = { 
            #    "timestamp": timestamp, 
            #    "esp32id": str(msgParser.getMsg().esp32id),
            #    "mp4id": str(msgParser.getMsg().mp1id),
            #    "mp4x": str(msgParser.getMsg().mp1canddb.x),
            #    "mp4y": str(msgParser.getMsg().mp1canddb.y),
            #    "mp4db": str(msgParser.getMsg().mp1canddb.db),
            #    "audioId": fileId
            #    }
            #    tmp = coll2.insert_one(tmpdict)
            #if not data:
                # if data is not received break
            #    break
            
            #print("from connected user: " + str(data))
            #data = input(' -> ')
            #conn.send(data.encode())  # send data to the client

        conn.close()  # close the connection

        
