
##BoundarySet holds the upper and lower bounds on the x and y axis in meters.
class BoundarySet(object):
#Constructor
    def __init__(self, x_low, x_high, y_low, y_high):  # In Meters
        self.x_low = x_low
        self.x_high = x_high
        self.y_low = y_low
        self.y_high = y_high

#Getters
    def get_x_low(self):
        return self.x_low
    def get_x_high(self):
        return self.x_high
    def get_y_low(self):
        return self.y_low
    def get_y_high(self):
        return self.y_high
#Setters
    def set_x_low(self, x_low):
        self.x_low = x_low
    def set_x_high(self, x_high):
        self.x_high = x_high
    def set_y_low(self, y_low):
        self.y_low = y_low
    def set_y_high(self, y_high):
        self.y_high = y_high

