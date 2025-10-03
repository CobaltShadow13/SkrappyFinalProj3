#LocalFamily Class
class LocalFamily(object):
#Constructor
    def __init__(self, name, total_size, tag_size, apriltag_family, pieces):
        self.name = name
        self.totalSize = total_size
        self.tagSize = tag_size
        self.aprltag_family= apriltag_family
        self.pieces = pieces
#Getters
    def get_name(self):
        return self.name
    def get_total_size(self):
        return self.totalSize
    def get_tag_size(self):
        return self.tagSize
    def get_tag_family(self):
        return self.aprltag_family
    def get_pieces(self):
        return self.pieces
#Setters
    def set_name(self, name):
        self.name = name
    def set_total_size(self, total_size):
        self.totalSize = total_size
    def set_tag_size(self, tag_size):
        self.tagSize = tag_size
    def set_apriltag_family(self, apriltag_family):
        self.aprltag_family = apriltag_family
    def set_pieces(self, pieces):
        self.pieces = pieces

###########################Hard Coded objects_rename For Now#########################
from backend_rename.database_rename.objects_rename.shapes import player_shape
from backend_rename.database_rename.objects_rename.shapes import board_shape
from backend_rename.database_rename.objects_rename.shapes import house_shape_3x3

house = LocalFamily("house", 100, 77.8, "tag25h9", house_shape_3x3)
board = LocalFamily("board", 100, 75, "tag16h5", board_shape)
player = LocalFamily("player", 100, 77.8, "tag36h11", player_shape)