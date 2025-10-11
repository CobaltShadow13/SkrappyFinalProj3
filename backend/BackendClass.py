import config
import database.objects.shapes
from backend.scripts.utilities.board_utilities.auto_sense_dimensions import auto_sense_dimensions
from backend.scripts.utilities.board_utilities.board_utilities import create_board
from backend.scripts.utilities.apriltag_utilities.local_family_utilities import initialize_families

class Backend(object):
    def __init__(self):
        tile_size = config.default_tile_size_in
        width, height = auto_sense_dimensions()

        self.board = create_board(width, height, tile_size)
        self.camera = config.default_camera
        if not config.save:
            self.families = initialize_families()
        else:
            self.families = initialize_families() ##Change to get the save later
#Getters
    def get_board(self):
        return self.board
    def get_camera(self):
        return self.camera
    def get_families(self):
        return self.families
    def get_shapes(self):
        return data.objects.shapes.shapes
#Setters
    def set_board(self, board):
        self.board = board
    def set_camera(self, camera):
        self.camera = camera
    def set_families(self, families):
        self.families = families