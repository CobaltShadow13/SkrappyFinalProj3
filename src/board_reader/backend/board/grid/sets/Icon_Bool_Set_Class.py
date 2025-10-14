#Icon Bool Set Class holds the 3 different boundary sets for borders, doors, and windows, as well as the center icon
#This references whether the icon is turned on based the shape of the tag.
class IconBoolSet(object):
#Constructor
    def __init__(self, border_bool_set, door_bool_set, windows_bool_set, center_icon_bool):
        self.center_icon_bool = center_icon_bool
        self.door_bool_set = door_bool_set
        self.windows_bool_set = windows_bool_set
        self.border_bool_set = border_bool_set
#Getters
    def get_door_bool_set(self):
        return self.door_bool_set
    def get_windows_bool_set(self):
        return self.windows_bool_set
    def get_border_bool_set(self):
        return self.border_bool_set
    def get_center_icon_bool(self):
        return self.center_icon_bool
#Setters
    def set_door_bool_set(self, door_bool_set):
        self.door_bool_set = door_bool_set
    def set_windows_bool_set(self, windows_bool_set):
        self.windows_bool_set = windows_bool_set
    def set_border_bool_set(self, border_bool_set):
        self.border_bool_set = border_bool_set
    def set_center_icon_bool(self, center_icon_bool):
        self.center_icon_bool = center_icon_bool
