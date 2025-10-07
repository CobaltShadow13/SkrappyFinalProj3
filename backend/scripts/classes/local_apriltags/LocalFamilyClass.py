#LocalFamily Class
class LocalFamily(object):
#Constructor
    def __init__(self, tag_family, unassigned_tags, assigned_tags, ):
        self.tag_family = tag_family
        self.unassigned_tags = unassigned_tags
        self.assigned_tags = assigned_tags
        self.assigned_tags_num = 0
#Getters
    def get_tag_family(self):
        return self.tag_family
    def get_unassigned_tags(self):
        return self.unassigned_tags
    def get_assigned_tags(self):
        return self.assigned_tags
    def get_assigned_tags_num(self):
        return self.assigned_tags_num

#Setters
    def set_tag_family(self, tag_family):
        self.tag_family = tag_family
    def set_unassigned_tags(self, unassigned_tags):
        self.unassigned_tags = unassigned_tags
    def set_assigned_tags(self, assigned_tags):
        self.assigned_tags = assigned_tags
    def set_assigned_tags_num(self, assigned_tags_num):
        self.assigned_tags_num = assigned_tags_num

    def assign_tag(self):
        if len(self.unassigned_tags) > 0:
            self.assigned_tags_num += 1
            return self.unassigned_tags.pop(0)
        else:
            return None
