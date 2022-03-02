'''
Keith Boehler, America Ship, 2022 Jan 19

Objective:  To read and oporate on 3d image metadata

Precond:    Files must be on disk. To initialize a string to the folder 
            and a string with the name of the image to be opened. 

Postcond:   Internal file handle to interact with the exif data of the 
            supplied image. 

Bugs:       From Ipython testing i feel the img.get_all() maye miss some things
            based on some returned messages like: 
            'unable to read tag '_interoperability_ifd_Pointer'
            Tho from opening a single image and looking at its metadata 
            both with python and web reader said feilds are not present
            
            I find it strange as https://gitlab.com/TNThieding/exif/-/blob/master/src/exif/_image.py
            makes the all_tags dict from the list_all() func
            
            
'''
from exif import Image
import pprint
import time

class THREE_D_META:
    metadata = dict()
    __img_dir = "/path/to/files/"
    __img_name = "3dpic.jpg.unset"
    __img_path = "unset" 

    def __init__(self, folder_path, img_name):
        self.__img_dir = folder_path
        self.__img_name = img_name
        self.__img_path = self.__img_dir + img_name
        
        with open(self.__img_path, 'rb') as image_file:
            working_img_h = Image(image_file)
        
        self.metadata = working_img_h.get_all()
        self.metadata.update({'Image Name' : img_name})
        '''
        for key in self.metadata:
            print(self.metadata[key])
            
        print(self.metadata['gps_longitude_ref'])
        time.sleep(30)'''

    def getImageDir(self):
        return self.__img_dir
    
    def getImageName(self):
        return self.__img_name
        
    def getHeader(self):
        return self.metadata
    
    def getLat(self):
        return self.metadata['gps_latitude']
    
    def getLong(self):
        return self.metadata['gps_longitude']
    
   # def getImageName(self):
    #    return self.metadata['Image Name']

    def getLatRef(self):
        return self.metadata['gps_latitude_ref']
    
    def getLongRef(self):
        return self.metadata['gps_longitude_ref']
    
    def dms2Decimal(self):
        """ 
        precond: Have succesfully run init
        postcond: Metadata attribute of latitude and longitude will be updated to
                    show their values in decimal rather than degrees.
        """
        dms_degree_lat = self.getLat()
        dms_degree_lat_ref = self.getLatRef()
        dms_degree_long = self.getLong()
        dms_degree_long_ref = self.getLongRef()
        #               hour                  minute                          seconds
        decimal_lat = dms_degree_lat[0] + dms_degree_lat[1] / 60 + dms_degree_lat[2] / 3600
        decimal_long = dms_degree_long[0] + dms_degree_long[1] / 60 + dms_degree_long[2] / 3600
        
        if dms_degree_lat_ref == "S":
            decimal_lat = -1*decimal_lat
        
        if dms_degree_long_ref == "W":
            decimal_long = -1*decimal_long
        
        self.metadata['gps_latitude'] = decimal_lat
        self.metadata['gps_longitude'] = decimal_long
        
    def showMeta(self):
        pprint.pprint(self.metadata)
    
