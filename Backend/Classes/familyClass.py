

class Family(object):

    def __init__(self, name, totalSize, tagSize, tagFamily, familyShape, pieces):
        self.name = name
        self.familyShape = familyShape
        self.totalSize = totalSize
        self.tagSize = tagSize
        self.tagFamily= tagFamily
        self.pieces = pieces

    def getName(self):
        return self.name

    def getTotalSize(self):
        return self.totalSize

    def getTagSize(self):
        return self.tagSize

    def getTagFamily(self):
        return self.tagFamily

    def getTagID(self):
        return self.tagID

    def getPieces(self):
        return self.pieces

    def setName(self, name):
        self.name = name

    def setTotalSize(self, totalSize):
        self.totalSize = totalSize

    def setTagSize(self, tagSize):
        self.tagSize = tagSize

    def setTagFamily(self, tagFamily):
        self.tagID = tagFamily

    def setPieces(self, pieces):
        self.pieces = pieces

###########################Hard Coded Objects For Now#########################
from Backend.Objects.shapes import playerShape
from Backend.Objects.shapes import boardShape
from Backend.Objects.shapes import houseShape

house = Family("house", 100, 77.8, "tag25h9", houseShape, [0] )
board = Family("board", 100, 75, "tag16h5", boardShape, [0,1,2,3])
player = Family("player", 100, 77.8, "tag36h11", playerShape, [0,1,2,3])