class BorderSet(object):
#Constructor
    def __init__(self, top_border=False, bottom_border=False, left_border=False, right_border=False):
        self.top_border = top_border
        self.bottom_border = bottom_border
        self.left_border = left_border
        self.right_border = right_border

#Getters
    def get_top_border(self):
        return self.top_border
    def get_bottom_border(self):
        return self.bottom_border
    def get_left_border(self):
        return self.left_border
    def get_right_border(self):
        return self.right_border
#Setters
    def set_top_border(self, top_border):
        self.top_border = top_border
    def set_bottom_border(self, bottom_border):
        self.bottom_border = bottom_border
    def set_left_border(self, left_border):
        self.left_border = left_border
    def set_right_border(self, right_border):
        self.right_border = right_border
