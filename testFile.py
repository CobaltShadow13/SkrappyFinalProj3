from MidEnd.Classes.gridClass import Grid
from MidEnd.HelperFunctions import *
from MidEnd.HelperFunctions.initializeGrid import initializeGrid



testGrid = Grid(initializeGrid(), 24, 24)

for x in range(0, 24):
    for y in range(0, 24):
        print(testGrid.getTile(y + 24 * x).tagID())

