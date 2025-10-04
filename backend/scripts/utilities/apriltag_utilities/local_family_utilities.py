import os

from backend.scripts.classes.local_apriltags.LocalFamilyClass import LocalFamily
import config
def initialize_families():
    families = []
    for dirs in config.directories:
        new_family = LocalFamily(os.path.dirname(dirs), [], [])
        for file in os.listdir(dirs):
            if file.endswith(".png"):
                new_family.get_unassigned_tags().append(file)
            else:
                continue
        families.append(new_family)
    detector_families = []
    for family in families:
        new_tfs = family.get_tag_family()
        detector_families.append(new_tfs)

    config.tag_family_strings = " ".join(detector_families)
    return families