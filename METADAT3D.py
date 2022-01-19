'''
Keith Boehler, America Ship
2022 Jan 19

Objective: To read and oporate on 3d image metadata
Precond:
Postcond:
Bugs:
'''

class THREE_D_META:
    metadata = dict()
    img_dir = "/path/to/files/"
    img_path = "3dpic.jpg"

    def __init__(self, folder_path, img_name):
        self.img_dir = folder_path
        self.img_path = self.img_path + img_name

