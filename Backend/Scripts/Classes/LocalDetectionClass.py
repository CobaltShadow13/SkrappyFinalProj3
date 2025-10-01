class LocalDetection(object):
    def __init__(self, local_detection, tile, x, y, z):
        self.local_detection = local_detection
        self.tile = tile
        self.x = x
        self.y = y
        self.z = z
#Getters
    def get_local_detection(self):
        return self.local_detection
    def get_tile(self):
        return self.tile
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_z(self):
        return self.z

#Setters
    def set_local_detection(self, local_detection):
        self.local_detection = local_detection
    def set_tile(self, tile):
        self.tile = tile
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def set_z(self, z):
        self.z = z