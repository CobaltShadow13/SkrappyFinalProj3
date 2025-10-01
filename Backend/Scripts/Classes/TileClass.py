class BorderSet(object):

    def __init__(self, top_border=False, bottom_border=False, left_border=False, right_border=False):
        self.topBorder = top_border
        self.bottomBorder = bottom_border
        self.leftBorder = left_border
        self.rightBorder = right_border

    def getTopBorder(self):
        return self.topBorder

    def getBottomBorder(self):
        return self.bottomBorder

    def getLeftBorder(self):
        return self.leftBorder

    def getRightBorder(self):
        return self.rightBorder

    def setTopBorder(self, topBorder):
        self.topBorder = topBorder

    def setBottomBorder(self, bottomBorder):
        self.bottomBorder = bottomBorder

    def setLeftBorder(self, leftBorder):
        self.leftBorder = leftBorder

    def setRightBorder(self, rightBorder):
        self.rightBorder = rightBorder


##BoundarySet holds the upper and lower bounds on the x and y axis in meters.
class BoundarySet(object):
    def __init__(self, x_low, x_high, y_low, y_high):  # In Meters
        self.x_low = x_low
        self.x_high = x_high
        self.y_low = y_low
        self.y_high = y_high

        ##getters and setters

    def getXLow(self):
        return self.x_low

    def get_x_high(self):
        return self.x_high

    def get_y_low(self):
        return self.y_low

    def get_y_high(self):
        return self.y_high

    def set_x_low(self, x_low):
        self.x_low = x_low

    def set_x_high(self, x_high):
        self.x_high = x_high

    def set_y_low(self, y_low):
        self.y_low = y_low

    def setYHigh(self, y_high):
        self.y_high = y_high


class Tile():
    def __init__(self, size, x_tile_coord, y_tile_coord, tile_id, boundary_set, x_meter_coord, y_meter_coord): #xtilecoord and ytilecoord are in meters
        self.size = size #in meters
        self.x_tile_coord = x_tile_coord
        self.y_tile_coord = y_tile_coord
        self.tile_id = tile_id
        self.has_tag = False
        self.boundarySet = boundary_set
        self.x_meter_coord = x_meter_coord
        self.y_meter_coord = y_meter_coord

    ## Getters and Setters ##
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

    def get_boundary(self, boundary_pos):
        if boundary_pos == 0:
            return self.boundarySet.getXLow()

        elif boundary_pos == 1:
            return self.boundarySet.get_x_high()

        elif boundary_pos == 2:
            return self.boundarySet.get_y_low()

        elif boundary_pos == 3:
            return self.boundarySet.get_y_high()
        else:
            return None
    def get_boundary_set(self):
        return self.boundarySet


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
    def setBoundary(self, boundary_pos, boundary):
        if boundary_pos == 0:
            self.boundarySet.set_x_low(boundary)
        elif boundary_pos == 1:
            self.boundarySet.set_x_high(boundary)
        elif boundary_pos == 2:
            self.boundarySet.set_y_low(boundary)
        elif boundary_pos == 3:
            self.boundarySet.setYHigh(boundary)
        else:
            self.boundarySet.set_x_low(0)
            self.boundarySet.set_x_high(0)
            self.boundarySet.set_y_low(0)
            self.boundarySet.setYHigh(0)


    def set_meter_coordinates(self, x_tile_coord, y_tile_coord): #sets the meter coordinates by multiplying the
        self.x_meter_coord = self.get_size() * x_tile_coord
        self.y_meter_coord = self.get_size() * y_tile_coord


    def auto_set_bounds(self): ##auto sets bounds for itself. MAKE SURE IT HAS A SIZE AND X AND Y COORDINATES ALREADY
        if self.get_x_meter_coord() / self.get_x_meter_coord() == 1: ###checking for positive vs negative to correctly set the high bound to the right/top and low bound to the left/bottom
            self.get_boundary(0).setXLow = (self.get_x_meter_coord() - self.get_size())
            self.get_boundary(1).setXHigh = (self.get_x_meter_coord())
        else:
            self.get_boundary(0).setXLow = (self.get_x_meter_coord())
            self.get_boundary(1).setXHigh = (self.get_x_meter_coord() + self.get_size)
        if self.get_y_meter_coord() / self.get_y_meter_coord() == 1: ###checking for positive vs negative to correctly set the high bound to the right/top and low bound to the left/bottom
            self.get_boundary(2).setYLow = (self.get_y_meter_coord() - self.get_size())
            self.get_boundary(3).setYHigh = (self.get_y_meter_coord())
        else:
            self.get_boundary(2).setYLow = (self.get_y_meter_coord())
            self.get_boundary(3).setYHigh = (self.get_y_meter_coord() + self.get_size)