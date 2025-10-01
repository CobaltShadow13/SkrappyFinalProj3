#Imports
    ## Classes
from backend.scripts.classes.LocalCameraClass import LocalCamera
from backend.scripts.classes.GridClass import initialize_grid
    ##Helper Functions
from backend.scripts.helper_functions.capture_frame import capture_frame
from backend.scripts.helper_functions.conversions import inch_to_meters

import cv2 as cv

def __main__():
    # Make the grid generalizable later (by that I mean detect the corners for width and height and ask the DM if those are correct, then allow them to change them in the UI
    tileSize = inch_to_meters(1)
    mapGrid = initialize_grid(24, 24, tileSize)

    while True:
        #runs the capture frame every x seconds
        mainCamera = LocalCamera(cv.VideoCapture(0), 0, 0, 0, 0, None)
        capture_frame(1, mainCamera)


__main__()
