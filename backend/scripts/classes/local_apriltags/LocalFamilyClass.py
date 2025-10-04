#LocalFamily Class
class LocalFamily(object):
#Constructor
    def __init__(self, tag_family, unassigned_tags, assigned_tags):
        self.tag_family = tag_family
        self.unassigned_tags = unassigned_tags
        self.assigned_tags = assigned_tags

#Getters
    def get_tag_family(self):
        return self.tag_family
    def get_unassigned_tags(self):
        return self.unassigned_tags
    def get_assigned_tags(self):
        return self.assigned_tags
#Setters
    def set_tag_family(self, tag_family):
        self.tag_family = tag_family
    def set_unassigned_tags(self, unassigned_tags):
        self.unassigned_tags = unassigned_tags
    def set_assigned_tags(self, assigned_tags):
        self.assigned_tags = assigned_tags