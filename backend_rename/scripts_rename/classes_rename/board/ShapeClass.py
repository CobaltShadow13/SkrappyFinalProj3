class Shape(object):
    def __init__(self, name, shape_matrix):
        self.name = name
        self.shape_matrix = shape_matrix

#Getters
    def get_name(self):
        return self.name
    def get_shape(self):
        return self.shape_matrix
#Setters
    def set_name(self, name):
        self.name = name
    def set_shape(self, shape_matrix):
        self.shape_matrix = shape_matrix
