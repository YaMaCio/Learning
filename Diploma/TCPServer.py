import socket
from pymongo import MongoClient
#import pymongo
import gridfs
from time import gmtime, strftime
from ctypes import *
from MsgParser import MsgParser
import json
import DBFunctions
import asyncio
import logging

class TCPServer:
    def __init__(self):
        self.host = "127.0.0.1" #socket.gethostname()
        self.port = 9876  # initiate port no above 1024
        self.myclient = MongoClient("mongodb+srv://vitaliyskromyda:test@clusterdb.4wu0t0a.mongodb.net/?retryWrites=true&w=majority&appName=clusterdb", port=27017)
        self.mydb = self.myclient["clusterdb"]
        self.fs = gridfs.GridFS(self.mydb, collection="files")
        self.coll1 = self.mydb["firstmsg"]
        self.coll2 = self.mydb["secondmsg"] 
        logging.basicConfig(level=logging.INFO, filename="TCPServer.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
        logging.info("Class TCPServer initialized")

    async def handle_client(self, reader, writer):
        #loop = asyncio.get_event_loop()
        #request = None
        logging.info("Client connected")
        addr = writer.get_extra_info('peername')
        msgParser = MsgParser()
        dataBuffer = bytearray()
        logging.info("Start reading")
        data = await reader.read(16384)
        dataBuffer.extend(data)
        cUByteArray = (c_ubyte * len(dataBuffer)).from_buffer_copy(dataBuffer)
        #while request != 'quit':
        #request = (await loop.sock_recv(client, 16384))
        msgParser.setMessage(cUByteArray)
        logging.info("Data parsing")
        msgParser.parsing()
        logging.info("Converting data...")
        if msgParser.getSize() < 8212:
            timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            tmpdict = loads(msgParser.getJSONString())
            tmpdict['timestamp'] = timestamp
            logging.info("Data formated")
            tmp = self.coll1.insert_one(tmpdict)
            logging.info("Data added to DB")
        else:
            timeInSec = time() - 5
            timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime(timeInSec))
            audio = []
            msgParser.getAudio(audio)
            uploadDataAsFile(audio, self.fs, timestamp + ".mp3")
            fileID = findFileInDB(self.mydb, self.fs, timestamp + ".mp3")
            tmpdict = loads(msgParser.getJSONString())
            tmpdict['timestamp'] = timestamp
            tmpdict['audioID'] = fileID
            logging.info("Data formated")
            tmp = self.coll2.insert_one(tmpdict)
            logging.info("Data added to DB")
        writer.close()
        #client.close()

    async def runServer(self):
        # get the hostname
        

        #server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        #server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        #server_socket.listen(300)
        #server_socket.setblocking(False)
        logging.info("Entered in runServer()")
        loop = asyncio.get_event_loop()
        server = await loop.create_server(self.handle_client, self.host, self.port)
        logging.info("Server created")
        await server.serve_forever()
        #conn, address = server_socket.accept()  # accept new connection
        #print("Connection from: " + str(address))
        #while True:
            #conn, address = await loop.sock_accept(server_socket)
            #loop.create_task(self.handle_client(client, mydb, fs, coll1, coll2))
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

        #conn.close()  # close the connection

        
