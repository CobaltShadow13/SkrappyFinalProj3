#These hold the icon paths per tile.

class IconFileSet(object):
#Constructor
    def __init__(self, wall_icon, center_icon, door_icon, window_border_icon):
        self.wall_icon = wall_icon
        self.center_icon = center_icon
        self.door_icon = door_icon
        self.window_border_icon = window_border_icon
#Getters
    def get_wall_icon(self):
        return self.wall_icon
    def get_center_icon(self):
        return self.center_icon
    def get_door_icon(self):
        return self.door_icon
    def get_window_border_icon(self):
        return self.window_border_icon
#Setters
    def set_wall_icon(self, wall_icon):
        self.wall_icon = wall_icon
    def set_center_icon(self, center_icon):
        self.center_icon = center_icon
    def set_door_icon(self, door_icon):
        self.door_icon = door_icon
    def set_window_border_icon(self, window_border_icon):
        self.window_border_icon = window_border_icon

