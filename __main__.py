from Backend.GridSystem import initializeGrid
from Backend.HelperFunctions.captureFrame import captureframe
from Backend.Classes.cameraClass import Camera
from Backend.GridSystem import initializeGrid
import cv2 as cv

def __main__():
    # Make the grid generalizable later (by that I mean detect the corners for width and height and ask the DM if those are correct, then allow them to change them in the UI
    mapGrid = initializeGrid(24, 24)
    while True:
        #runs the capture frame every x seconds
        mainCamera = Camera(cv.VideoCapture(0), 0,0,0,0, None)
        captureframe(1, mainCamera)


__main__()
