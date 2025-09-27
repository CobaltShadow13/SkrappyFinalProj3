class BorderSet(object):

    def __init__(self, topBorder=False, bottomBorder=False, leftBorder=False, rightBorder=False):
        self.topBorder = topBorder
        self.bottomBorder = bottomBorder
        self.leftBorder = leftBorder
        self.rightBorder = rightBorder

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
    def __init__(self, xLow, xHigh, yLow, yHigh):  # In Meters
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
    def __init__(self,size , xTileCoord, yTileCoord, tileID, boundarySet):
        self.size = size #in meters
        self.xTileCoord = xTileCoord
        self.yTileCoord = yTileCoord
        self.tileID = tileID
        self.hasTag = False
        self.boundarySet = boundarySet

    ## Getters and Setters ##
    def getSize(self):
        return self.size
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

    def getBoundary(self, boundaryPos):
        if boundaryPos == 0:
            return self.boundarySet.getXLow()

        elif boundaryPos == 1:
            return self.boundarySet.getXHigh()

        elif boundaryPos == 2:
            return self.boundarySet.getYLow()

        elif boundaryPos == 3:
            return (self.boundarySet.getYHigh())
        else:
            return None
    def setSize(self, size):
        self.size = size

    def setXTileCoord(self, xTileCoord):
        self.xTileCoord = xTileCoord

    def setYTileCoord(self, yTileCoord):
        self.yTileCoord = yTileCoord

    def setHasTag(self, hasTag):
        self.hasTag = hasTag

    def setTileID(self, y, width, x):
        tileID = y + width * x
        self.tileID = tileID

    def setBoundary(self, boundaryPos, boundary):
        if boundaryPos == 0:
            self.boundarySet.setXLow(boundary)
        elif boundaryPos == 1:
            self.boundarySet.setXHigh(boundary)
        elif boundaryPos == 2:
            self.boundarySet.setYLow(boundary)
        elif boundaryPos == 3:
            self.boundarySet.setYHigh(boundary)
        else:
            self.boundarySet.setXLow(0)
            self.boundarySet.setXHigh(0)
            self.boundarySet.setYLow(0)
            self.boundarySet.setYHigh(0)

    def autoSetBounds(self):
        self.setBoundary(0, self.getXCoord()-self.getSize())
        self.setBoundary(1, self.getXCoord())
        self.setBoundary(2, self.getYCoord()-self.getSize())
        self.setBoundary(3, self.getYCoord())
