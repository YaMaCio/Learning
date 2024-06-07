import pyforms
from pyforms.basewidget import BaseWidget
#from pyforms.controls   import ControlFile
from pyforms.controls   import ControlText
#from pyforms.controls   import ControlSlider
#from pyforms.controls   import ControlPlayer
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlList
from pyforms import start_app
from Triangle           import Triangle
from TriangleController import TriangleController
from PostController     import PostController
#from TCPServer          import TCPServer
import asyncio
import logging

class Server(BaseWidget, TriangleController, PostController):
    def __init__(self, *args, **kwargs):
        logging.info("Initializing")
        BaseWidget.__init__(self, 'Server')
        TriangleController.__init__(self)
        PostController.__init__(self)
        #self._loop = asyncio.get_event_loop()
        logging.info("Class Server initialized")

        #Definition of the forms fields
        self._tmpTriangle     = Triangle('-1', '-1', '-1', '-1')
        self._triangleID    = ControlText('Triangle ID')
        self._firstVertex    = ControlText('First vertex ID')
        self._secondVertex    = ControlText('Second vertex ID')
        self._thirdVertex    = ControlText('Third vertex ID')
        self._list        = ControlList('Triangles List')
        self._removeButton     = ControlButton('Remove')
        self._addButton     = ControlButton('Add')
        self._changeButton     = ControlButton('Change')
        self._importButton     = ControlButton('Import dump')
        self._exportButton     = ControlButton('Export dump')
        
        self._postList        = ControlList('Post List')
        self._refresh = ControlButton('Refresh')

        self._list.horizontal_headers = ['Triangle ID', 'Vertex 1', 'Vertex 2', 'Vertex 3']
        self._postList.horizontal_headers = ['Post ID', 'Timestamp', 'Triangle ID', 'Latitude', 'Longitude', 'Address', 'Audio ID']
        self._postList.readonly = True
        #Define the function that will be called when a file is selected
        #self._videofile.changed_event     = self.__videoFileSelectionEvent
        #Define the event that will be called when the run button is processed
        #self._refreshMessagesTask = _loop.create_task(self.__refreshMessages)
        self._removeButton.value       = self.__removeEvent
        self._changeButton.value       = self.__changeEvent
        self._addButton.value       = self.__addEvent
        self._refresh.value = self.__refreshMessages
        #Define the event called before showing the image in the player

        #Define the organization of the Form Controls
        self._formset = [{
            'a:Triangles':[('_triangleID', '_firstVertex', '_secondVertex', '_thirdVertex'),
            ('_removeButton', '_changeButton', '_addButton'),
            ('_list', ('_importButton', '=', '_exportButton'))],
            'b:Messages':['_postList', '_refresh']
        }]

        eventServerInitialized.set()
    
    def __refreshMessages(self):
        logging.info("Start refreshing messages")
        super(Server, self).calculateTriangles(super(Server, self).getTriangles())
        posts = super(Server, self).getPosts()
        trianglesIDs = []
        for i in range(0, self._postList.rows_count-1):
            trianglesIDs.append(self._postList.get_value(3, i))
        for post in posts:
            if post._triangleID not in trianglesIDs:
                self._postList += [post._postID, post._timestamp, post._triangleID, post._latitude, post._longitude, post._address, post._audioID]
        trianglesIDs.clear()
        posts.clear()
        logging.info("End refreshing messages")
    
    #@classmethod
    #async def __refreshMessages(cls):
    #    while True:
    #        logging.info("Start refreshing messages")
    #        super(Server, cls).calculateTriangles(super(Server, cls).getTriangles())
    #        posts = super(Server, cls).getPosts()
    #        postsIDs = []
    #        for i in range(0, cls._postList.rows_count-1):
    #            postsIDs.append(cls._postList.get_value(1, i))
    #        for post in posts:
    #            if post._postID not in postsIDs:
    #                cls._postList += [post._postID, post._timestamp, post._triangleID, post._latitude, post._longitude, post._address, post._audioID]
    #        postsIDs.clear()
    #        posts.clear()
    #    logging.info("End refreshing messages")
    
    def addTriangleToList(self, triangle):
        """
        Reimplement the addPerson function from People class to update the GUI
        everytime a new person is added.
        """
        super(Server, self).addTriangle(triangle)
        self._list += [triangle._triangleID, triangle._firstVertex, triangle._secondVertex, triangle._thirdVertex]

    def removeTriangleFromList(self, index):
        """
        Reimplement the removePerson function from People class to update the GUI
        everytime a person is removed.
        """
        super(Server, self).removeTriangle(index)
        self._list -= index

    def __changeEvent(self):
        """
        Remove person button event
        """
        self.removeTriangleFromList( self._list.selected_row_index )

    def __addEvent(self):
        """
        Add person button event.
        """
        #self._tmpTriangle._triangleID             = self._triangleID.value
        #self._tmpTriangle._firstVertex            = self._firstVertex.value
        #self._tmpTriangle._secondVertex           = self._secondVertex.value
        #self._tmpTriangle._thirdVertex            = self._thirdVertex.value
        self.addTriangleToList(Triangle(
            self._triangleID.value,
            self._firstVertex.value,
            self._secondVertex.value,
            self._thirdVertex.value
        ))

    def __removeEvent(self):
        """
        Remove person button event
        """
        self.removeTriangleFromList( self._list.selected_row_index )

async def waitInit():
    await eventServerInitialized.wait()
    await asyncio.sleep(3)

async def main():
    #loop = asyncio.get_running_loop()
    #loop.set_debug(True)
    logging.info("Entered in main()")
    #logging.info("Started TCPServer thread")
    blockingTask = asyncio.to_thread(start_app, Server)
    #asyncio.create_task(start_app(Server)))
    #to_thread(start_app, Server))
    #await asyncio.sleep(20)
    #task2 = asyncio.create_task(blockingTask)
    task1 = asyncio.to_thread(waitInit)
    logging.info("Started ServerGUI thread")
    await task1
    task2 = asyncio.create_task(Server.__refreshMessages())
    #await asyncio.gather(start_app(server), server.runServer())
    await task2
    await blockingTask

if __name__ == '__main__':
    global eventServerInitialized
    eventServerInitialized = asyncio.Event()
    logging.basicConfig(level=logging.DEBUG, filename="serverGUI.log", filemode="w",
                        format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info("Starting ServerGUI")
    start_app(Server)
    #server = Server
    #tcpsFunc = tcpServer.runServer
    #asyncio.run(main(), debug = True)