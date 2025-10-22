import config


class Tile:
#Constructor
    def __init__(self, size:float, x_tile_coord, y_tile_coord, tile_id, boundary_set, icon_display_set, x_meter_coord: float, y_meter_coord: float):
        self.size = size #in meters
        self.x_tile_coord = x_tile_coord
        self.y_tile_coord = y_tile_coord
        self.tile_id = tile_id
        self.has_tag = False
        self.boundary_set = boundary_set
        self.icon_display_set = icon_display_set
        self.x_meter_coord = x_meter_coord #in meters
        self.y_meter_coord = y_meter_coord #in meters
#Getters
    def get_size(self):
        return self.size
    def get_x_tile_coord(self):
        return self.x_tile_coord
    def get_y_tile_coord(self):
        return self.y_tile_coord
    def get_x_meter_coord(self):
        return self.x_meter_coord
    def get_y_meter_coord(self):
        return self.y_meter_coord
    def get_tile_id(self):
        return self.tile_id
    def get_row(self, width):
        return self.tile_id / width
    def get_col(self, height):
        return self.tile_id % height
    def get_has_tag(self):
        return self.has_tag
    def get_boundary_set(self):
        return self.boundary_set
    def get_icon_display_set(self):
        return self.icon_display_set
    def get_pixel_boundary_set(self):
        return self.pixel_boundary_set
#Setters
    def set_size(self, size):
        self.size = size
    def set_x_tile_coord(self, x_tile_coord):
        self.x_tile_coord = x_tile_coord
    def set_y_tile_coord(self, y_tile_coord):
        self.y_tile_coord = y_tile_coord
    def set_x_meter_coord(self, x_meter_coord):
        self.x_meter_coord = x_meter_coord
    def set_y_meter_coord(self, y_meter_coord):
        self.y_meter_coord = y_meter_coord
    def set_has_tag(self, has_tag):
        self.has_tag = has_tag
    def set_tile_id(self, y, width, x):
        tileID = y + width * x
        self.tile_id = tileID
    def set_boundary_set(self, boundary_set):
        self.boundary_set = boundary_set
    def set_pixel_boundary_set(self, pixel_boundary_set):
        self.pixel_boundary_set = pixel_boundary_set
    def set_icon_display_set(self, icon_display_set):
        self.icon_display_set = icon_display_set
    def set_meter_coordinates(self, x_tile_coord, y_tile_coord): #sets the meter coordinates by multiplying the
        self.x_meter_coord = self.get_size() * x_tile_coord
        self.y_meter_coord = self.get_size() * y_tile_coord
    def auto_set_bounds(self): ##auto sets bounds for itself. MAKE SURE IT HAS A SIZE AND X AND Y COORDINATES ALREADY
        if self.get_x_meter_coord() >= 0: ###checking for positive vs negative to correctly set the high bound to the right/top and low bound to the left/bottom
            self.get_boundary_set().set_x_low((self.get_x_meter_coord() - self.get_size()))
            self.get_boundary_set().set_x_high(self.get_x_meter_coord())
        else:
            self.get_boundary_set().set_x_low(self.get_x_meter_coord())
            self.get_boundary_set().set_x_high(self.get_x_meter_coord() + self.get_size())

        if self.get_y_meter_coord() >= 0: ###checking for positive vs negative to correctly set the high bound to the right/top and low bound to the left/bottom
            self.get_boundary_set().set_y_low(self.get_y_meter_coord() - self.get_size())
            self.get_boundary_set().set_y_high(self.get_y_meter_coord())
        else:
            self.get_boundary_set().set_y_low(self.get_y_meter_coord())
            self.get_boundary_set().set_y_high(self.get_y_meter_coord() + self.get_size())
