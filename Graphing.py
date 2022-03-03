'''
Keith Boehler, 2022 March 1

Objective: Create Directed Graphs to simulate 3d tour. The glue for the nodes in GraphingNodes

PreCond:

PostCond:

Bugs:

'''
from METADAT3D import THREE_D_META


class Graphing:
    __tour_guide_location = "empty"
    __nodes_dict = dict()
    
    def __init__(self, tour_spots, tour_enterance = "none"):
        self.tourSpotsUpdater(tour_spots)
        self.__tour_guide_location = tour_enterance
    
    
    def tourSpotsUpdater(self, new_spot):
        """:param new_spot: New spot for the tour. Will be a dicionary with name of photo as key
        and the value of the obj address (node)
        
        precond: image 3d data has been loaded into node
        
        postcond: dictorary of nodes is longer with the new entery :)
        
        bugs: 
        
        """
        self.__nodes_dict.update(new_spot)

    def moveLocation(self):
        possible_moves = self.__tour_guide_location.getNeigborhood()
        i = 0
        tmp = dict()
        for place in possible_moves:
            print(i, " : ", place)
            tmp.update({i : possible_moves[place]})
            i = i + 1
        user = input("Select number for next room:  ")
        user = int(user)
        self.__tour_guide_location = self.__nodes_dict[tmp[user].getImageName()]

    def getTourLocation(self):
        return self.__tour_guide_location.whoAmI()
