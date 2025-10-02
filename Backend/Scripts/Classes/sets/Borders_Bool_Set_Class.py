class BorderBoolSet(object):
    def __init__(self, north, south, east, west):
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    # Getters
    def get_north(self):
        return self.north

    def get_south(self):
        return self.south

    def get_east(self):
        return self.east

    def get_west(self):
        return self.west

    # Setters
    def set_north(self, north):
        self.north = north

    def set_south(self, south):
        self.south = south

    def set_east(self, east):
        self.east = east

    def set_west(self, west):
        self.west = west