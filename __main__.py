from Backend.GridSystem import initializeGrid
from Backend.HelperFunctions.captureFrame import captureframe
from Backend.Classes.cameraClass import Camera
from Backend.GridSystem import initializeGrid
import cv2 as cv

def __main__():
    # Make the grid generalizable later
    mapGrid = initializeGrid(24, 24)
    while True:
        #runs the capture frame every x seconds
        mainCamera = Camera(cv.VideoCapture(0), 0,0,0,0, None)
        captureframe(1, mainCamera)


__main__()
