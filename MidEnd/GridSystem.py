class Tile():
    def __init__(self, xCoord, yCoord, tileID):
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.tileID = tileID

    ## Getters and Setters ##
    def getXCoord(self):
        return self.xCoord
    def getYCoord(self):
        return self.yCoord
    def getTileID(self):
        return self.tileID
    def getRow(self, width):
        return (self.tileID / width)
    def getCol(self, height):
        return (self.tileID % height)

    def setXCoord(self, xCoord):
        self.xCoord = xCoord
    def setYCoord(self, yCoord):
        self.yCoord = yCoord


def setTileID(y, width, x):
    tileID = y + width * x
    return tileID

def setTileMap(width, height):
    tileMap = []
    xOffset = width / 2
    yOffset = height / 2

    ## set the unique tileID that will allow us to call the row or col with one number as well as the grid system
    for x in range(width):
        column = []
        for y in range(height):
            tileID = setTileID(y, width, x)
            xCoord = x - xOffset
            yCoord = y - yOffset
            tileMap.append(Tile(xCoord, yCoord, tileID))




    return tileMap


class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tileMap = setTileMap(width, height)

    ## Getters and Setters
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def getTileMap(self):
        return self.tileMap

    def setWidth(self, width):
        self.width = width
    def setHeight(self, height):
        self.height = height



def initializeGrid(width, height):
    grid = Grid(width, height)
    return grid


grid = initializeGrid(24,24)