import os
from METADAT3D import THREE_D_META



def loadPicsList(dir):    
    """ Get the pics from disk to mem
    :param dir: The parth to the folder with the 3d images of interest.     
    postcond:
    """ 
    pics_list = os.listdir(dir)
    for i in range(len(pics_list)):
        pic = THREE_D_META(dir, pics_list[i])
        pics_list[i] = pic
    return pics_list

def prepPlot(pics_list):
    """ Trim down the data in meme to min needed for plotting
    :param pics_list: The metadata of images loaded into mem from loadPicsList()
                        Names will be index 0, latitude index 1 and longitude index 2
    postcond: 
    """
    dats = []
    for i in range(len(pics)):
        tmp = [pics[i].getImageName(), pics[i].getLat(), pics[i].getLong()]
        dats.append(tmp) 
    return dats

def mapBounderies(dat):
    """ Create a box for the map
    :param dat: list contaning name, lat and long. 
    
    Postcond: 
    """
pics_dir = "/mnt/c/Users/AS/Pictures/America Ship 3D/"

pics = loadPicsList(pics_dir)
pics = prepPlot(pics)

lats = pics[::][:1]
print(lats)

