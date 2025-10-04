#Imports

from backend.scripts.utilities.board_utilities.grid_utilities.tilemap_utilities import  create_tile_map


#Grid Class
class Grid(object):
#Constructor
    def __init__(self, width, height, x_meter_coord, y_meter_coord, tile_size):
        self.width = width
        self.height = height
        self.tileMap = create_tile_map(width, height, x_meter_coord, y_meter_coord, tile_size)
        self.x_meter_coord = x_meter_coord
        self.y_meter_coord = y_meter_coord
        self.filled_tiles = []
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
    def get_tile(self, tile_id):
        return self.get_tile_map()[tile_id]
    def get_filled_tiles(self):
        return self.filled_tiles
#Setters
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def set_x_meter_coord(self, x_meter_width):
        self.x_meter_coord = x_meter_width
    def set_y_meter_coord(self, y_meter_height):
        self.y_meter_coord = y_meter_height
    def set_filled_tiles(self, filled_tiles):
        self.filled_tiles = filled_tiles

#Helper Functions
    def update_grid(self, tags):
        tile_map = self.get_tile_map()
        has_tile_array = []
        for current_tile in tile_map:
                for tag in tags:
                    in_x_low = False
                    in_x_high = False
                    in_y_low = False
                    in_y_high = False

                    if tag.get_x() < current_tile.get_boundary_set().get_x_high():
                        if tag.get_y() < current_tile.get_boundary_set().get_y_high():
                            if tag.get_y() >= current_tile.get_boundary_set().get_y_low():
                                if tag.get_x() >= current_tile.get_boundary_set().get_x_low():
                                    in_x_low = True
                                    in_x_high = True
                                    in_y_low = True
                                    in_y_high = True

                    if in_x_low and in_x_high and in_y_low and in_y_high:
                        current_tile.set_has_tag(True)
                        tags[tag].set_tile(current_tile)
                        has_tile_array.append(current_tile.get_tile_id())
        self.set_filled_tiles(has_tile_array)






##initialize_grid helper function
def initialize_grid(width, height, tile_size):
    grid = Grid(width, height, tile_size*width, tile_size*height, tile_size) ##this should work
    return grid
