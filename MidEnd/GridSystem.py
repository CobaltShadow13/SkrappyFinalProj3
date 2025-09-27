
##BoundarySet holds the upper and lower bounds on the x and y axis in meters.
class BoundarySet(object):
    def __init__(self, xLow, xHigh, yLow, yHigh): #In Meters
        self.xLow = xLow
        self.xHigh = xHigh
        self.yLow = yLow
        self.yHigh = yHigh

        ##getters and setters
        def getXLow(self):
            return self.xLow
        def getXHigh(self):
            return self.xHigh
        def getYLow(self):
            return self.yLow
        def getYHigh(self):
            return self.yHigh

        def setXLow(self, xLow):
            self.xLow = xLow
        def setXHigh(self, xHigh):
            self.xHigh = xHigh
        def setYLow(self, yLow):
            self.yLow = yLow
        def setYHigh(self, yHigh):
            self.yHigh = yHigh




class Tile():
    def __init__(self, xTileCoord, yTileCoord, tileID, boundarySet):
        self.xTileCoord = xTileCoord
        self.yTileCoord = yTileCoord
        self.tileID = tileID
        self.hasTag = False
        self.boundarySet = boundarySet

    ## Getters and Setters ##
    def getXCoord(self):
        return self.xTileCoord
    def getYCoord(self):
        return self.yTileCoord
    def getTileID(self):
        return self.tileID
    def getRow(self, width):
        return (self.tileID / width)
    def getCol(self, height):
        return (self.tileID % height)
    def getHasTag(self):
        return self.hasTag

    def setXTileCoord(self, xTileCoord):
        self.xTileCoord = xTileCoord
    def setYTileCoord(self, yTileCoord):
        self.yTileCoord = yTileCoord
    def setHasTag(self, hasTag):
        self.hasTag = hasTag
    def setTileID(self, y, width, x):
        tileID = y + width * x
        self.tileID = tileID





def setTileMap(tileMap, width, height):
    xTileCoordOffset = width / 2
    yTileCoordOffset = height / 2

    ## set the unique tileID that will allow us to call the row or col with one number as well as the grid system
    for x in range(width):
        column = []
        for y in range(height):
            tileMap[y][x].setXTileCoord(x - xTileCoordOffset)
            tileMap[y][x].setYTileCoord(y - yTileCoordOffset)
            tileMap[y][x].setTileID(y, width, x)
            print("Tile ID:", tileMap[y][x].getTileID())
            print("X: ", tileMap[y][x].getXCoord())
            print(" Y: ", tileMap[y][x].getYCoord())



def createTileMap(width, height):
    newTileMap = []
    for x in range(width):
        column = []
        for y in range(height):
            column.append(Tile(None, None, None, None))
        newTileMap.append(column)
    setTileMap(newTileMap, width, height)
    return newTileMap


class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tileMap = createTileMap(width, height)

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