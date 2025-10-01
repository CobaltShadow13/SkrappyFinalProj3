###################################################Tilemap Helper Functions
def set_tile_map(tile_map, width, height):  ##this function sets the grid coordinates to a +- cartesian coordinate system as well as other functions of the tilemap.
    xTileCoordOffset = width / 2
    yTileCoordOffset = height / 2

    ## set the unique tileID that will allow us to call the row or col with one number as well as the grid system
    for x in range(width):
        column = []
        for y in range(height):
            tile_map[y][x].set_x_tile_coord(x - xTileCoordOffset)
            tile_map[y][x].set_y_tile_coord(y - yTileCoordOffset)
            tile_map[y][x].set_tile_id(y, width, x)
            tile_map[y][x].auto_set_bounds()

            print("Tile ID:", tile_map[y][x].get_tile_id())
            print("X: ", tile_map[y][x].get_x_coord())
            print(" Y: ", tile_map[y][x].get_y_coord())

def create_tile_map(width, height, width_m:float, height_m:float, tile_size):
    new_tile_map = []
    for x in range(width):
        column = []
        for y in range(height):
            boundary_set = BoundarySet(0,0,0,0)
            border_set = BorderSet(0,0,0,0)
            new_tile = Tile(tile_size, None, None, None, boundary_set, border_set, width_m, height_m)
            column.append(new_tile)

        new_tile_map.append(column)
    set_tile_map(new_tile_map, width, height)
    return new_tile_map