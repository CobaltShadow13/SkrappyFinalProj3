#Btoard Piece Class


class BoardPiece(object):
#Constructor
    def __init__(self, name, apriltag_family, shape, tag_num, tag_image):
        self.name = name
        self.dir = dir
        self.apriltag_family = apriltag_family
        self.shape = shape
        self.tag_num = tag_num
        self.tag_image = tag_image

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



#Helper Functinos
######################################################################################################################################################################################