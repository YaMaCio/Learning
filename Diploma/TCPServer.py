import socket
from ctypes import *

class TCPServer:
    def server_program():
        # get the hostname
        msgParser = MsgParser()
        host = socket.gethostname()
        port = 9999  # initiate port no above 1024

        server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        server_socket.listen(300)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 10240 bytes
            data = conn.recv(16384)
            msgParser.setMsg(data)
            
            #if not data:
                # if data is not received break
            #    break
            
            print("from connected user: " + str(data))
            #data = input(' -> ')
            #conn.send(data.encode())  # send data to the client

        conn.close()  # close the connection

    def parsing:
        
