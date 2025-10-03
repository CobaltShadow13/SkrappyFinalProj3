#Imports
    ## Classes
from backend.scripts.classes.local_opencv.LocalCameraClass import LocalCamera
from backend.scripts.classes.Board.grid.GridClass import initialize_grid
    ##Helper Functions
from backend.scripts.utilities.apriltag_utilities.capture_frame import capture_frame
from backend.scripts.utilities.general_utilities.conversions import inch_to_meters
from backend.database.objects.detectors import board_detector


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
