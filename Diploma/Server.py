import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls   import ControlFile
from pyforms.controls   import ControlText
from pyforms.controls   import ControlSlider
from pyforms.controls   import ControlPlayer
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlList
from Triangle           import Triangle
from TriangleController import TriangleController
from TCPServer          import TCPServer

class Server(TriangleController, BaseWidget):

    def __init__(self, *args, **kwargs):
        TriangleController.__init__(self)
        BaseWidget.__init__(self,'Server')

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

        self._list.horizontal_headers = ['Triangle ID', 'Vertex 1', 'Vertex 2', 'Vertex 3']
        #Define the function that will be called when a file is selected
        #self._videofile.changed_event     = self.__videoFileSelectionEvent
        #Define the event that will be called when the run button is processed
        self._removeButton.value       = self.__removeEvent
        self._changeButton.value       = self.__changeEvent
        self._addButton.value       = self.__addEvent
        #Define the event called before showing the image in the player

        #Define the organization of the Form Controls
        self._formset = [{
            'a:Triangles':[('_triangleID', '_firstVertex', '_secondVertex', '_thirdVertex'),
            ('_removeButton', '_changeButton', '_addButton'),
            ('_list', ('_importButton', '=', '_exportButton'))],
            'b:Messages':[]
        }]


    #def __videoFileSelectionEvent(self):
        """
        When the videofile is selected instanciate the video in the player
        """
    #    self._player.value = self._videofile.value

    #def __process_frame(self, frame):
        """
        Do some processing to the frame and return the result frame
        """
    #    return frame
    
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
        self._tmpTriangle._triangleID             = self._triangleID.value
        self._tmpTriangle._firstVertex            = self._firstVertex.value
        self._tmpTriangle._secondVertex           = self._secondVertex.value
        self._tmpTriangle._thirdVertex            = self._thirdVertex.value
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


if __name__ == '__main__':

    from pyforms import start_app
    start_app(Server)