#Imports
from backend.scripts.helper_functions.tilemap import  create_tile_map
#Grid Class
class Grid(object):
#Constructor
    def __init__(self, width, height, x_meter_coord, y_meter_coord, tile_size):
        self.width = width
        self.height = height
        self.tileMap = create_tile_map(width, height, x_meter_coord, y_meter_coord, tile_size)
        self.x_meter_coord = x_meter_coord
        self.y_meter_coord = y_meter_coord
#Getters
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_tile_map(self):
        return self.tileMap
    def get_x_meter_coord(self):
        return self.x_meter_coord
    def get_y_meter_coord(self):
        return self.y_meter_coord
#Setters
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def set_x_meter_coord(self, x_meter_width):
        self.x_meter_coord = x_meter_width
    def set_y_meter_coord(self, y_meter_height):
        self.y_meter_coord = y_meter_height

##initialize_grid helper function
def initialize_grid(width, height, tile_size):
    grid = Grid(width, height, tile_size*width, tile_size*height, tile_size) ##this should work
    return grid
