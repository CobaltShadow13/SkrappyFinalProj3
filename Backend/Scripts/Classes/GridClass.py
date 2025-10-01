##Border set holds the boolean values for turning on and off the border walls in the UI
from Backend.Scripts.Classes.TileClass import Tile, BoundarySet


def set_tile_map(tile_map, width, height): ##this function sets the grid coordinates to a +- cartesian coordinate system.
    xTileCoordOffset = width / 2
    yTileCoordOffset = height / 2

    ## set the unique tileID that will allow us to call the row or col with one number as well as the grid system
    for x in range(width):
        column = []
        for y in range(height):
            tile_map[y][x].set_x_tile_coord(x - xTileCoordOffset)
            tile_map[y][x].set_y_tile_coord(y - yTileCoordOffset)
            tile_map[y][x].set_tile_id(y, width, x)
            print("Tile ID:", tile_map[y][x].get_tile_id())
            print("X: ", tile_map[y][x].get_x_coord())
            print(" Y: ", tile_map[y][x].get_y_coord())



def create_tile_map(width, height, width_m, height_m):
    newTileMap = []
    for x in range(width):
        column = []
        for y in range(height):
            boundarySet = BoundarySet(0,0,0,0)
            newTile = Tile(None, None, None, None, boundarySet, width_m, height_m)
            column.append(newTile)
            newTileMap[y][x].auto_set_bounds()
        newTileMap.append(column)
    set_tile_map(newTileMap, width, height)
    return newTileMap


class Grid(object):
    def __init__(self, width, height, x_meter_width, y_meter_height):
        self.width = width
        self.height = height
        self.tileMap = create_tile_map(width, height, x_meter_width, y_meter_height)

    ## Getters and Setters
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_tile_map(self):
        return self.tileMap

    def set_width(self, width):
        self.width = width
    def setHeight(self, height):
        self.height = height


def initialize_grid(width, height, tile_size):
    grid = Grid(width, height, tile_size, tile_size) ##this should work
    return grid
