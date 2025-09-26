class BoardPiece(object):

    def __init__(self, name, family, shape, totalSize, tagSize, tagID):
        self.name = name
        self.family = family
        self.shape = shape
        self.tagID = tagID
        self.totalSize = totalSize
        self.tagSize = tagSize

## Getters and Setters ##

    def getname(self):
        return self.name

    def getfamily(self):
        return self.family

    def getshape(self):
        return self.shape

    def gettagID(self):
        return self.tagID

    def gettotalSize(self):
        return self.totalSize

    def gettagSize(self):
        return self.tagSize


    def setname(self, name):
        self.name = name

    def setfamily(self, family):
        self.family = family

    def setshape(self, shape):
        self.shape = shape

    def settagID(self, tagID):
        self.tagID = tagID

    def settotalSize(self, totalSize):
        self.totalSize = totalSize

    def settagSize(self, tagSize):
        self.tagSize = tagSize
######################################################################################################################################################################################