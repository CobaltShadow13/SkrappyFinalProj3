from Backend.HelperFunctions.detectAprilTags import captureframe
from Backend.Classes.cameraClass import Camera
import cv2 as cv

def __main__():
    while True:
        #runs the capture frame every 30 seconds
        mainCamera = Camera(cv.VideoCapture(0), 0,0,0,0, None)

        captureframe(1, mainCamera)


__main__()
