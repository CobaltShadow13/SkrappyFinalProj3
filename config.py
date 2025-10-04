from backend.scripts.classes.board.grid.sets.Icon_File_Set_Class import IconFileSet
from backend.scripts.utilities.general_utilities.conversions import inch_to_meters
from backend.scripts.classes.local_opencv.LocalCameraClass import LocalCamera
import cv2 as cv

#Default Icons
default_door_icon = "default_door.png"
default_wall_icon = "default_wall.png"
default_center_icon = "default_center.png"
default_window_border_icon = "default_window.png"
defaultIconFileSet = IconFileSet(default_wall_icon, default_center_icon, default_door_icon, default_window_border_icon)


product_width = 24.0 #Tiles
product_height = 24.0 #Tiles

prototype_width = 6.0 #Tiles
prototype_height = 6.0 #Tiles

default_tile_size = inch_to_meters(1)

default_camera = LocalCamera(cv.VideoCapture(0), 0, 0, 0, 0, None)