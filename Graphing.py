'''
Keith Boehler, 2022 March 1

Objective: Create Directed Graphs to simulate 3d tour. The glue for the nodes in GraphingNodes

PreCond:

PostCond:

Bugs:

'''
from METADAT3D import THREE_D_META


class graphing:
    __tour_guide_location = "empty"
    __nodes_dict = dict()
    
    def __init__(self, tour_spots, tour_enterance = "none"):
        self.tour_spots_updater(tour_spots)
        self.__tour_guide_location = tour_enterance
    
    
    def tour_spots_updater(self, new_spot):
    """:param new_spot: New spot for the tour. Will be a dicionary with name of photo as key
        and the value of the obj address (node)
        
        precond: image 3d data has been loaded into node
        
        postcond: dictorary of nodes is longer with the new entery :)
        
        bugs: 
        
        """
        self.__nodes_dict.update(new_spot)

    def move_location(self):
        possible_moves = self.__tour_guide_location.getNeigborhood()
        i = 0
        tmp = dict()
        for place in possible_moves:
            print(i, " : ", place)
            tmp.update({i : place})
            i = i + 1
        user = input("Select number for next room:  ")
        __tour_guide_location = tmp[user]

