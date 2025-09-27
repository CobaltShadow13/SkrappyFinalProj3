# For Grid
# You could indeed use numpy for this.
# One way would be to define a 3d array as np.zeros((x_coor, y_coor, 2))
# and save each of the coordinates along the last axis.

class Grid(object):
    def __init__(self, width, height, grid):
        self.width = width
        self.height = height
        self.grid = grid

## Getters and Setters ##

    def getwidth(self):
        return self.width

    def getheight(self):
        return self.height

    def getgrid(self):
        return self.grid

    def setwidth(self, width):
        self.width = width

    def setheight(self, height):
        self.height = height

    def setgrid(self, grid):
        self.grid = grid

    def getTile(self, tileID):
        return self.grid[tileID // 24, tileID % 24]



#helper functions
    def updategrid(self):
        pass








