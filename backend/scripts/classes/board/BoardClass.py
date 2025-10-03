class Board(object):
    def __init__(self, grid, detection_array):
        self.grid = grid
        self.detection_array = detection_array

#Getters
    def get_grid(self):
        return self.grid
    def get_detection_array(self):
        return self.detection_array

#Setters
    def set_grid(self, grid):
        self.grid = grid
    def set_detection_array(self, detection_array):
        self.detection_array = detection_array
