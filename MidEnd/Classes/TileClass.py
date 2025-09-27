import numpy as np


class Tile(object):
#1

#If you know width of the grid - it is Wdt tiles wide, then
    #N = Col + Wdt * Row
#To retrieve tile coordinates from number:
    #Col = N % Wdt      //integer modulo
    #Row = N // Wdt      //integer division


    def __init__(self, xValue, yValue, tagID,
                 xLowBound_m, yLowBound_m,
                 xHighBound_m, yHighBound_m,
                 hasTag, tag=None
                 ):

        self.xValue = xValue
        self.yValue = yValue

        self.tagID = tagID

        self.xLowBound_m = xLowBound_m
        self.yLowBound_m = yLowBound_m
        self.xHighBound_m = xHighBound_m
        self.yHighBound_m = yHighBound_m

        self.hasTag = hasTag
        self.tag = tag


## getters and setters
    def getxTile(self):
        return self.x
    def getyTile(self):
        return self.y
    def getxLowBound_m(self):
        return self.xLowBound_m
    def getyLowBound_m(self):
        return self.yLowBound_m
    def getxHighBound_m(self):
        return self.xHighBound_m
    def getyHighBound_m(self):
        return self.yHighBound_m
    def gethasTag(self):
        return self.hasTag
    def gettag(self):
        return self.tag

    def setxTile(self, x):
        self.x = x
    def setyTile(self, y):
        self.y = y
    def setxLowBound_m(self, x):
        self.xLowBound_m = x
    def setyLowBound_m(self, y):
        self.yLowBound_m = y
    def setxHighBound_m(self, x):
        self.xHighBound_m = x
    def setyHighBound_m(self, y):
        self.yHighBound_m = y
    def sethasTag(self, hasTag):
        self.hasTag = hasTag
    def settag(self, tag):
        self.tag = tag

    ###############################

    #Helper Functions







