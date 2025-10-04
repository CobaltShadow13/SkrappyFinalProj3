#Board Piece Class
from backend.scripts.utilities.general_utilities.conversions import convert_to_apriltag_path

class BoardPiece(object):
#Constructor
    def __init__(self, name, apriltag_family, shape, tag_num, tag_image):
        self.name = name
        self.apriltag_family = apriltag_family
        self.shape = shape
        self.tag_num = tag_num
        self.tag_image = tag_image
        self.set_dir()
# Getters
    def get_name(self):
        return self.name
    def get_apriltag_family(self):
        return self.apriltag_family
    def get_shape(self):
        return self.shape
    def get_tag_num(self):
        return self.tag_num
    def get_tag_image(self):
        return self.tag_image
#Setters
    def set_name(self, name):
        self.name = name
    def set_apriltag_family(self, family):
        self.apriltag_family = family
    def set_shape(self, shape):
        self.shape = shape
    def set_tag_num(self, tag_id):
        self.tag_num = tag_id
    def set_tag_image(self, tag_image):
        self.tag_image = tag_image
    def set_dir(self):
        base_directory = self.get_apriltag_family().get_directory()
        tag_num = self.get_tag_num()
        tag_family = self.get_apriltag_family()
        convert_to_apriltag_path(base_directory,tag_family, tag_num)

#Helper Functinos
######################################################################################################################################################################################