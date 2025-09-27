from MidEnd.Classes.TileClass import Tile


def initializeGrid(grid, xTiles, yTiles):


## Ben Idea to work on next:
    # Multiple multidimensional assignments to retrieve the grid
        #create a unique id to them via the method in tileclass.
        #make get and set defs for those things reflect that method
        #
        #

    tileList = list()

    for x in range(1, grid.width+1):
        for y in range(1,grid.height+1):
            xValue = None
            yValue = None
            tagID = y + xTiles * x
            xLowBound = None
            yLowBound = None
            xHighBound = None
            yHighBound = None
            hasTag = False

            newTile = Tile(xValue, yValue, tagID,
                           xLowBound, yLowBound,
                           xHighBound, yHighBound,
                           hasTag)

            tileList.append(newTile)




    return tileList




