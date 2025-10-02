#Icon Bool Set Class
from backend.scripts.classes.sets.Borders_Bool_Set_Class import BorderBoolSet
from backend.scripts.classes.sets.Doors_Bool_Set_Class import DoorBoolSet
from backend.scripts.classes.sets.Windows_Bool_Set_Class import WindowsBoolSet

class IconBoolSet(object):
#Constructor
    def __init__(self, border_bool_set:BorderBoolSet, door_bool_set:DoorBoolSet, windows_bool_set:WindowsBoolSet, center_icon_bool):
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
