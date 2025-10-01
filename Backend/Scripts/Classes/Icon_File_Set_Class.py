class IconFileSet(object):
    def __init__(self, top_border_icon, bottom_border_icon, right_border_icon, left_border_icon, center_icon):
        self.top_border_icon = top_border_icon
        self.left_border_icon = left_border_icon
        self.right_border_icon = right_border_icon
        self.bottom_border_icon = bottom_border_icon
        self.center_icon = center_icon

#Getters
    def get_top_border(self):
        return self.top_border_icon
    def get_left_border(self):
        return self.left_border_icon
    def get_right_border(self):
        return self.right_border_icon
    def get_bottom_border(self):
        return self.bottom_border_icon
    def get_center_icon(self):
        return self.center_icon

#Setters
    def set_top_border(self, top_border_icon):
        self.top_border_icon = top_border_icon
    def set_left_border(self, left_border_icon):
        self.left_border_icon = left_border_icon
    def set_right_border(self, right_border_icon):
        self.right_border_icon = right_border_icon
    def set_bottom_border(self, bottom_border_icon):
        self.bottom_border_icon = bottom_border_icon
    def set_center_icon(self, center_icon):
        self.center_icon = center_icon
