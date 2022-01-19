'''
Keith Boehler, America Ship, 2022 Jan 19

Objective:  To read and oporate on 3d image metadata

Precond:    Files must be on disk. To initialize a string to the folder 
            and a string with the name of the image to be opened. 

Postcond:   Internal file handle to interact with the exif data of the 
            supplied image. 

Bugs:
'''
from exif import Image

class THREE_D_META:
    metadata = dict()
    __img_dir = "/path/to/files/"
    __img_name = "3dpic.jpg"
    __img_path = " " 

    def __init__(self, folder_path, img_name):
        self.__img_dir = folder_path
        self.__img_name = img_name
        self.__img_path = self.__img_dir + img_name
        
        with open(self.__img_path, 'rb') as image_file:
            working_img_h = Image(image_file)
        
        self.metadata = working_img_h.list_all()

    def getImageDir(self):
        return self.__img_dir
    
    def getImageName(self):
        return self.__img_name
        
    def getHeader(self):
        return self.metadata



    