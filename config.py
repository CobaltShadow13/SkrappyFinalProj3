from backend.scripts.classes.board.grid.sets.Icon_File_Set_Class import IconFileSet
from backend.scripts.utilities.general_utilities.conversions import inch_to_meters
from backend.scripts.classes.local_opencv.LocalCameraClass import LocalCamera
import cv2 as cv

#Has been saved
save = False
save_dir = None

tag_family_strings = "tag16h5"
camera_calibration_path = r"D:\SERAPH_AI\SkrappyFinalProj3\backend\scripts\classes\local_opencv\camera_calibration_library\scripts\data\calibration\camera_intrinsics\fisheye_calibration.json"


#Default Icons
default_door_icon = "default_door.png"
default_wall_icon = "default_wall.png"
default_center_icon = "default_center.png"
default_window_border_icon = "default_window.png"
defaultIconFileSet = IconFileSet(default_wall_icon, default_center_icon, default_door_icon, default_window_border_icon)

product_width = 24.0  #Tiles
product_height = 24.0  #Tiles

prototype_width = 6.0  #Tiles
prototype_height = 6.0  #Tiles

default_tile_size_in = inch_to_meters(1)
default_tile_size_mm = inch_to_meters(1) * 1000
default_tag_size_mm = 19.6 #mm (with padding)

default_camera = LocalCamera(cv.VideoCapture(0))

#Default Tag Family Directories
base_family_dir = r"D:\SERAPH_AI\SkrappyFinalProj3\database\assets\apriltag-imgs-master"


