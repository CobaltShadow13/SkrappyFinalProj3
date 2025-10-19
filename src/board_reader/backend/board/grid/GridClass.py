#Imports

from src.board_reader.backend.board.grid.utils.tilemap_utilities import create_tile_map ##import the create tile map helper function.


#Grid Class
class Grid(object):
#Constructor
    def __init__(self, width, height, x_meter_coord, y_meter_coord, tile_size): #Could afford to make the variable naming less confusing for this class.
        self.width = width #Takes in a width in tiles
        self.height = height #Takes in a width in tiles
        self.tileMap = create_tile_map(width, height, x_meter_coord, y_meter_coord, tile_size) #utilizing the inputted width, height, and x and y meter lengths
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


    def update_grid(self, tags, board_piece_array):
        new_tags = []
        #Cull the list of tags based off of the player inputted board pieces
        for tag in tags:
            for board_piece in board_piece_array:
                if tag.get_local_detection().tag_id == board_piece.get_tag_num() & tag.get_local_detection().tag_image == board_piece.get_local_detection().tag_family == board_piece.get_apriltag_family().get_tag_family():
                    new_tags.append(tag)
        tags = new_tags
        #Reset tilemap for new detections
        tile_map = self.get_tile_map()
        for tile in tile_map:
            tile.set_has_tag(False)

        has_tile_array = []
        for current_tile in tile_map:
                for tag in tags:
                    in_x_low = False
                    in_x_high = False
                    in_y_low = False
                    in_y_high = False

                    if tag.get_x() < current_tile.get_boundary_set().get_x_high() * 1000: #if the local detections x val is less than the right x boundary converted to mm
                        if tag.get_y() < current_tile.get_boundary_set().get_y_high() * 1000: #if the local detections y val is less than the top y boundary converted to mm
                            if tag.get_y() >= current_tile.get_boundary_set().get_y_low() * 1000: #if the local detections y val is greater than or equal to the bottom y boundary converted to mm
                                if tag.get_x() >= current_tile.get_boundary_set().get_x_low() * 1000: #if the local detections x val is greater than the left x boundary converted to mm
                                    in_x_low = True
                                    in_x_high = True
                                    in_y_low = True
                                    in_y_high = True

                    if in_x_low and in_x_high and in_y_low and in_y_high:
                        current_tile.set_has_tag(True)
                        tag.set_tile(current_tile)
                        has_tile_array.append(current_tile.get_tile_id())
                    else:
                        current_tile.set_has_tag(False)



        self.set_filled_tiles(has_tile_array)





##initialize_grid helper function
def initialize_grid(width, height, tile_size):
    grid = Grid(width, height, tile_size*width, tile_size*height, tile_size) ##this should work
    return grid
