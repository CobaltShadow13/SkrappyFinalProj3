from HelperFunctions.detectAprilTags import captureframe
from Classes.cameraClass import Camera
import cv2 as cv


while True:
    #runs the capture frame every 30 seconds
    mainCamera = Camera(cv.VideoCapture(0), 0,0,0,0, None)

    captureframe(1, mainCamera)
