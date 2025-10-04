import config
from backend.scripts.utilities.board_utilities.auto_sense_dimensions import auto_sense_dimensions
from backend.scripts.utilities.board_utilities.board_utilities import create_board

class Backend(object):
    def __init__(self):
        tile_size = config.default_tile_size
        width, height = auto_sense_dimensions()
        self.board = create_board(width, height, tile_size)
        self.camera = config.default_camera

#Getters
    def get_board(self):
        return self.board
    def get_camera(self):
        return self.camera
#Setters
