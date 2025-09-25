class BoardPiece(object):

    def __init__(self, name, family, shape):
        self.name = name
        self.family = family
        self.shape = shape

## Getters and Setters ##

    def getname(self):
        return self.name

    def getfamily(self):
        return self.family

    def getshape(self):
        return self.shape

    def setname(self, name):
        self.name = name

    def setfamily(self, family):
        self.family = family

    def setshape(self, shape):
        self.shape = shape
######################################################################################################################################################################################