import os
from METADAT3D import THREE_D_META
import numpy as np
import matplotlib.pyplot as plt

def loadPicsList(dir):    
    """ Get the pics from disk to mem
    :param dir: The parth to the folder with the 3d images of interest.     
    precond:
    postcond:
    """ 
    pics_list = os.listdir(dir)
    for i in range(len(pics_list)):
        pic = THREE_D_META(dir, pics_list[i])
        pics_list[i] = pic
        pics_list[i].dms2Decimal()
    return pics_list

def prepPlot(pics_list):
    """ Trim down the data in meme to min needed for plotting
    :param pics_list: The metadata of images loaded into mem from loadPicsList()
                        Names will be index 0, latitude index 1 and longitude index 2
                        for lat reference 3 and long reference 4
    precond: 
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
    precond:
    Postcond: 
    """
    lats = np.zeros(len(dat))
    longs = np.zeros(len(dat))
    for i in range(len(dat)):
        # As per prepPlot() 1 is for latitude and 2 is for longitude
        lats[i] = dat[i][1] 
        longs[i] = dat[i][2]
    lats.sort()
    longs.sort()
    boundry_box = [longs[0], longs[len(longs)-1], lats[0], lats[len(lats)-1]]
    return boundry_box, lats, longs

    
pics_dir = "/mnt/c/Users/AS/Pictures/America Ship 3D/"

pics = loadPicsList(pics_dir)
pics = prepPlot(pics)
b, lats, longs = mapBounderies(pics)
map = plt.imread("/mnt/c/Users/AS/src/Cam/data/map.png")
print(b)

fig, ax = plt.subplots()
ax.scatter(longs, lats)
print(lats)
ax.set_title("AS 3d Tour")
ax.set_xlim(b[0], b[1])
ax.set_ylim(b[2], b[3])

ax.imshow(map, zorder=0, extent = b, aspect='equal')