#Icon Display Set Class holds the icon bool set and the files for each tile.
class IconDisplaySet(object):
#Constructor
    def __init__(self, icon_bool_set, icon_file_set):
        self.icon_bool_set = icon_bool_set
        self.icon_file_set = icon_file_set
#Getters
    def get_icon_bool_set(self):
        return self.icon_bool_set
    def get_icon_file_set(self):
        return self.icon_file_set
#Setters
    def set_icon_bool_set(self, icon_bool_set):
        self.icon_bool_set = icon_bool_set
    def set_icon_file_set(self, icon_file_set):
        self.icon_file_set = icon_file_set

