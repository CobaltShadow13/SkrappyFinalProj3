################################################### Tilemap Helper Functions
from backend.scripts.classes.board.grid.TileClass import Tile
from backend.scripts.classes.board.grid.sets.TileBoolSetClass import TileBoolSet
from backend.scripts.classes.board.grid.sets.Icon_Display_Set_Class import IconDisplaySet
from backend.scripts.classes.board.grid.sets.BoundarySetClass import BoundarySet
from backend.scripts.classes.board.grid.sets.Icon_Bool_Set_Class import IconBoolSet
import config

def set_tile_map(tile_map, width, height):#Sets various functions of the tilemap
    xTileCoordOffset = width / 2
    yTileCoordOffset = height / 2

    for x in range(int(width)):
        column = []
        for y in range(int(height)):
            newTile = tile_map[y][x]

            newTile.set_x_tile_coord(x - xTileCoordOffset)
            newTile.set_y_tile_coord(y - yTileCoordOffset)
            newTile.set_tile_id(y, width, x)
            newTile.set_meter_coordinates(newTile.get_x_tile_coord(), newTile.get_y_tile_coord())
            newTile.auto_set_bounds()

            print("Tile ID:", tile_map[y][x].get_tile_id())
            print("X: ", tile_map[y][x].get_x_tile_coord())
            print("Y: ", tile_map[y][x].get_y_tile_coord())


def reindex_by_tile_id(new_tile_map, width, height):
    tile_id_index = []
    for x in range(int(width)):
        for y in range(int(height)):
            tile_id_index.append(new_tile_map[x][y])

    return tile_id_index



def create_tile_map(width, height, width_m:float, height_m:float, tile_size):
    new_tile_map = []
    for x in range(int(width)):
        column = []
        for y in range(int(height)):
            boundary_set = BoundarySet(0,0,0,0)
            border_bool_set = TileBoolSet(False, False, False, False)
            center_icon_bool = False
            icon_file_set = config.defaultIconFileSet
            icon_bool_set = IconBoolSet(border_bool_set, border_bool_set, border_bool_set, center_icon_bool)
            icon_display_set = IconDisplaySet(icon_bool_set, icon_file_set)
            new_tile = Tile(tile_size, None, None, None, boundary_set, icon_display_set, width_m, height_m)
            column.append(new_tile)

        new_tile_map.append(column)
    set_tile_map(new_tile_map, width, height)
    new_tile_map = reindex_by_tile_id(new_tile_map, width, height)

    return new_tile_map