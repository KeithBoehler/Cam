import numpy as np
from exif import Image


print("hello")
img_dir = "/mnt/c/Users/AS/Pictures/America Ship 3D/"
img_path1 = img_dir + "R0012338.JPG"



with open(img_path1, 'rb') as image_file:
    my_image = Image(image_file)
    
print(img_path1)
print(my_image.gps_latitude)
print(my_image.gps_longitude)



img_path1 = img_dir + "R0012343.JPG"
with open(img_path1, 'rb') as image_file:
    my_image2 = Image(image_file)
    
print(img_path1)
print(my_image2.gps_latitude)
print(my_image2.gps_longitude)


img_path1 = img_dir + "R0012369.JPG"
with open(img_path1, 'rb') as image_file:
    my_image3 = Image(image_file)
    
print(img_path1)
print(my_image3.gps_latitude)
print(my_image3.gps_longitude)
