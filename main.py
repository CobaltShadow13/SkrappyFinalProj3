from HelperFunctions.detectAprilTags import captureframe
from cameraClass import Camera
import cv2 as cv


while True:
    #runs the capture frame every 30 seconds
    mainCamera = Camera()
    mainCamera.loadCalibration()
    mainCamera.setCamera(cv.VideoCapture(0))

    captureframe(1, mainCamera)
