'''
Keith Boehler, 2022 March 1

Objective: Create Directed Graphs Nodes to simulate 3d tour.

PreCond: Image metadata has already be loaded into meme with the METADAT3D.py

PostCond: A node that knows who is next to itself

Bugs:

'''

from pprint import pprint 

class TourNodes:
    active_node = "empty"
    __neighbor_nodes = dict()
    
    def __init__(self, new_node):
        self.active_node = new_node

    def addNeighbor(self, adjacent_node):
        """:param adjacent_node: This is a node that is able to be reached from the active node.
    It is of data type <METADAT3D.THREE_D_META object at 0x7f189856ffd0>
    """
        self.__neighbor_nodes.update({adjacent_node.getImageName(): adjacent_node})
    
    def getNeigborhood(self):
        return __neighbor_nodes
    
    
    # some debuging methods
    def showActiveNode(self):
        print(self.active_node)
        
    def showNeighborhood(self):
        pprint(self.__neighbor_nodes)


