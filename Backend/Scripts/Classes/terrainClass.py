class BoardPiece(object):

    def __init__(self, name, family, shape, total_size, tag_size, tag_id):
        self.name = name
        self.family = family
        self.shape = shape
        self.tagID = tag_id
        self.totalSize = total_size
        self.tagSize = tag_size

## Getters and Setters ##

    def get_name(self):
        return self.name

    def get_family(self):
        return self.family

    def get_shape(self):
        return self.shape

    def get_tag_id(self):
        return self.tagID

    def get_total_size(self):
        return self.totalSize

    def get_tag_size(self):
        return self.tagSize


    def set_name(self, name):
        self.name = name

    def set_family(self, family):
        self.family = family

    def set_shape(self, shape):
        self.shape = shape

    def set_tag_id(self, tag_id):
        self.tagID = tag_id

    def set_total_size(self, total_size):
        self.totalSize = total_size

    def set_tag_size(self, tag_size):
        self.tagSize = tag_size
######################################################################################################################################################################################