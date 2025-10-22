from src.board_reader.backend.board.grid.sets.Icon_File_Set_Class import IconFileSet
from src.board_reader.backend.utils.conversions import inch_to_meters
from src.board_reader.backend.local_opencv.LocalCameraClass import LocalCamera
import cv2 as cv

#Has been saved
save = False
save_dir = None

tag_family_strings = "tag16h5"
camera_calibration_path = r"src\camera_calibration\scripts\data\calibration\camera_intrinsics\fisheye_calibration.json"


#Default Icons
default_door_icon = "default_door.png"
default_wall_icon = "default_wall.png"
default_center_icon = "default_center.png"
default_window_border_icon = "default_window.png"
defaultIconFileSet = IconFileSet(default_wall_icon, default_center_icon, default_door_icon, default_window_border_icon)

product_width = 6.0  #Tiles
product_height = 6.0  #Tiles

prototype_width = 6.0  #Tiles
prototype_height = 6.0  #Tiles

default_tile_size_in = inch_to_meters(1) ##Rename this to tile size in meters
default_tile_size_mm = inch_to_meters(1) * 1000
default_tag_size_mm = .005 #mm (with padding)

#Main camera object, change this to 1,2,3 etc for different cameras plugged into the computer.
default_camera = LocalCamera(cv.VideoCapture(0))

#Default Tag Family Directories
base_family_dir = r"src\board_reader\data\assets\apriltag-imgs-master"


