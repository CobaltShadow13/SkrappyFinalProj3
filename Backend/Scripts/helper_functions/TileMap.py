###################################################Tilemap Helper Functions
from backend.scripts.classes.TileClass import Tile
from backend.scripts.classes.IconDisplaySet import IconDisplaySet
from backend.scripts.classes.BoundarySetClass import BoundarySet

def set_tile_map(tile_map, width, height):#Sets various functions of the tilemap
    xTileCoordOffset = width / 2
    yTileCoordOffset = height / 2

    for x in range(width):
        column = []
        for y in range(height):
            tile_map[y][x].set_x_tile_coord(x - xTileCoordOffset)
            tile_map[y][x].set_y_tile_coord(y - yTileCoordOffset)
            tile_map[y][x].set_tile_id(y, width, x)
            tile_map[y][x].auto_set_bounds()

            print("Tile ID:", tile_map[y][x].get_tile_id())
            print("X: ", tile_map[y][x].get_x_tile_coord())
            print("Y: ", tile_map[y][x].get_y_tile_coord())


def create_tile_map(width, height, width_m:float, height_m:float, tile_size):
    new_tile_map = []
    for x in range(width):
        column = []
        for y in range(height):
            boundary_set = BoundarySet(0,0,0,0)
            border_set = IconDisplaySet(False, False, False, False, False)
            new_tile = Tile(tile_size, None, None, None, boundary_set, border_set, width_m, height_m)
            column.append(new_tile)

        new_tile_map.append(column)
    set_tile_map(new_tile_map, width, height)
    return new_tile_map