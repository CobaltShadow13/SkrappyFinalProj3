from Backend.Scripts.HelperFunctions.captureFrame import capture_frame
from Backend.Scripts.Classes.cameraClass import Camera
from Backend.Scripts.Classes.GridClass import initialize_grid
import cv2 as cv

def __main__():
    # Make the grid generalizable later (by that I mean detect the corners for width and height and ask the DM if those are correct, then allow them to change them in the UI
    mapGrid = initialize_grid(24, 24)
    while True:
        #runs the capture frame every x seconds
        mainCamera = Camera(cv.VideoCapture(0), 0,0,0,0, None)
        capture_frame(1, mainCamera)


__main__()
