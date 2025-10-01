##Border set holds the boolean values for turning on and off the border walls in the UI
from Backend.Scripts.Classes.TileClass import Tile, BoundarySet


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
            boundarySet = BoundarySet(0,0,0,0)
            column.append(Tile(None, None, None, None, boundarySet))
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
