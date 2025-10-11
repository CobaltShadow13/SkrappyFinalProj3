from src.board_reader.backend.local_apriltags.LocalFamilyClass import LocalFamily
import config
import os

def initialize_families():
    families = []
    base_dir = config.base_family_dir

    for dirs in os.listdir(base_dir):
        dir_path = os.path.join(base_dir, dirs)
        if not os.path.isdir(dir_path):
            continue  # skip files, only keep folders

        png_files = [f for f in os.listdir(dir_path) if f.endswith(".png")]

        new_family = LocalFamily(os.path.basename(dir_path), png_files, [])
        families.append(new_family)


    config.tag_family_strings = " ".join(f.get_tag_family() for f in families)
    return families
