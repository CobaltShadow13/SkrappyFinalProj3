class Family(object):
    def __init__(self, name, totalSize, tagSize, tagFamily, tagID, pieces):
        self.name = name
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

    def setTagID(self, tagID):
        self.tagID = tagID

    def setPieces(self, pieces):
        self.pieces = pieces

###########################Objects#########################

house = Family("house", 100, 77.8, "tag25h9", [0])
board = Family("board", 100, 75, "tag16h5", [0,1,2,3])
player = Family("player", 100, 77.8, "tag36h11", [0,1,2,3])