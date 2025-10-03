#Imports
    ## Classes
from backend_rename.scripts_rename.classes_rename.local_opencv.LocalCameraClass import LocalCamera
from backend_rename.scripts_rename.classes_rename.grid.GridClass import initialize_grid
    ##Helper Functions
from backend_rename.scripts_rename.utilities.apriltag_utilities.capture_frame import capture_frame
from backend_rename.scripts_rename.utilities.general_utilities.conversions import inch_to_meters
from backend_rename.database_rename.objects_rename.detectors import board_detector


import cv2 as cv

def __main__():
    # Make the grid generalizable later (by that I mean detect the corners for width and height and ask the DM if those are correct, then allow them to change them in the UI
    tileSize = inch_to_meters(1)
    mapGrid = initialize_grid(24.0, 24.0, tileSize)

    while True:
        #runs the capture frame every x seconds
        mainCamera = LocalCamera(cv.VideoCapture(0), 0, 0, 0, 0, None)
        detection_tags = capture_frame(1, mainCamera, board_detector)
        mapGrid.update_grid(detection_tags)


__main__()
