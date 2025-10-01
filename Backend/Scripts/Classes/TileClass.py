from Backend.Scripts.Classes.BorderSetClass import BorderSet
from Backend.Scripts.Classes.BoundarySetClass import BoundarySet

class Tile:
#Constructor
    def __init__(self, size:float, x_tile_coord, y_tile_coord, tile_id, boundary_set, border_set, x_meter_coord: float, y_meter_coord: float):
        self.size = size #in meters
        self.x_tile_coord = x_tile_coord
        self.y_tile_coord = y_tile_coord
        self.tile_id = tile_id
        self.has_tag = False
        self.boundary_set = boundary_set
        self.border_set = border_set
        self.x_meter_coord = x_meter_coord #in meters
        self.y_meter_coord = y_meter_coord #in meters

#Getters
    def get_size(self):
        return self.size
    def get_x_coord(self):
        return self.x_tile_coord
    def get_y_coord(self):
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
    def get_boundary(self, boundary_pos): ##get a specific boundary lmfao
        if boundary_pos == 0:
            return self.boundary_set.get_x_low()
        elif boundary_pos == 1:
            return self.boundary_set.get_x_high()
        elif boundary_pos == 2:
            return self.boundary_set.get_y_low()
        elif boundary_pos == 3:
            return self.boundary_set.get_y_high()
        else:
            return None
    def get_border(self, border_pos):
        if border_pos == 0:
            return self.border_set.get_top_border()
        elif border_pos == 1:
            return self.border_set.get_bottom_border()
        elif border_pos == 2:
            return self.border_set.get_left_border()
        elif border_pos == 3:
            return self.border_set.get_right_border()
        else:
            return None
    def get_boundary_set(self):
        return self.boundary_set
    def get_border_set(self):
        return self.border_set
##Setters
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
    def set_boundary(self, boundary_pos, boundary):
        if boundary_pos == 0:
            self.boundary_set.set_x_low(boundary)
        elif boundary_pos == 1:
            self.boundary_set.set_x_high(boundary)
        elif boundary_pos == 2:
            self.boundary_set.set_y_low(boundary)
        elif boundary_pos == 3:
            self.boundary_set.set_y_high(boundary)
        else:
            self.boundary_set.set_x_low(0)
            self.boundary_set.set_x_high(0)
            self.boundary_set.set_y_low(0)
            self.boundary_set.set_y_high(0)
    def set_border(self, border_pos, border):
        if border_pos == 0:
            self.border_set.set_top_border(border)
        elif border_pos == 1:
            self.border_set.set_bottom_border(border)
        elif border_pos == 2:
            self.border_set.set_left_border(border)
        elif border_pos == 3:
            self.border_set.set_right_border(border)
        else:
            self.border_set.set_x_low(0)
            self.border_set.set_x_high(0)
            self.border_set.set_y_low(0)
            self.border_set.set_y_high(0)
    def set_meter_coordinates(self, x_tile_coord, y_tile_coord): #sets the meter coordinates by multiplying the
        self.x_meter_coord = self.get_size() * x_tile_coord
        self.y_meter_coord = self.get_size() * y_tile_coord
    def auto_set_bounds(self): ##auto sets bounds for itself. MAKE SURE IT HAS A SIZE AND X AND Y COORDINATES ALREADY
        if self.get_x_meter_coord() / self.get_x_meter_coord() == 1: ###checking for positive vs negative to correctly set the high bound to the right/top and low bound to the left/bottom
            self.get_boundary_set().set_x_low(self.get_x_meter_coord() - self.get_size())
            self.get_boundary_set().set_x_high(self.get_x_meter_coord())
        else:
            self.get_boundary_set().set_x_low(self.get_x_meter_coord())
            self.get_boundary_set().set_x_high(self.get_x_meter_coord() + self.get_size())
        if self.get_y_meter_coord() / self.get_y_meter_coord() == 1: ###checking for positive vs negative to correctly set the high bound to the right/top and low bound to the left/bottom
            self.get_boundary_set().set_y_low = (self.get_y_meter_coord() - self.get_size())
            self.get_boundary_set().set_y_high = (self.get_y_meter_coord())
        else:
            self.get_boundary_set().set_y_low = (self.get_y_meter_coord())
            self.get_boundary_set().set_y_high = (self.get_y_meter_coord() + self.get_size())

