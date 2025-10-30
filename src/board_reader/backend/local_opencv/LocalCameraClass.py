import json

import cv2 as cv
import numpy as np
import glob
import os

#Hard coded values for tuning the calibration for prototyping purposes
fx_multiplier = 1.0
fy_multiplier = 1.0
cx_multiplier = 1.0
cy_multiplier = 1.0


#https://calib.io/pages/camera-calibration-pattern-generator

class LocalCamera(object):
    def __init__(self, camera):
        self.camera = camera
        self.fx = None
        self.fy = None
        self.cx = None
        self.cy = None
        self.dist = None
        self.loadCalibration()

    ### Getters and Setters ###
    def getCamera(self):
        return self.camera

    def getfx(self):
        return self.fx

    def getfy(self):
        return self.fy

    def getcx(self):
        return self.cx

    def getcy(self):
        return self.cy

    def getdist(self):
        return self.dist

    def setCamera(self, camera):
        self.camera = camera

    def setfx(self, fx):
        self.fx = fx

    def setfy(self, fy):
        self.fy = fy

    def setcx(self, cx):
        self.cx = cx

    def setcy(self, cy):
        self.cy = cy

    def setdist(self, dist): self.dist = dist

    def getCameraMatrix(self):
        """Return full 3x3 intrinsic matrix K"""
        return np.array([[self.fx, 0, self.cx],
                         [0, self.fy, self.cy],
                         [0,      0,     1]])

    ### Helper Functions ###
    def calibrate_camera(self):
        pass

    def undistortImage(self, img):
        h, w = img.shape[:2]
        mtx = self.getCameraMatrix()
        newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, self.dist, (w, h), 1, (w, h))
        return cv.undistort(img, mtx, self.dist, None, newcameramtx)

    def loadCalibration(self):
        # Load JSON calibration
        camera_calibration_path = r"/data\calibration\camera_intrinsics\fisheye_calibration.json"
        filename = camera_calibration_path
        with open(filename, 'r') as f:
            data = json.load(f)

        mtx = np.array(data["K"])
        dist = np.array(data["D"])

        # Set parameters
        self.setfx(mtx[0, 0] * fx_multiplier)
        self.setfy(mtx[1, 1] * fy_multiplier)
        self.setcx(mtx[0, 2] * cx_multiplier)
        self.setcy(mtx[1, 2] * cy_multiplier)
        self.setdist(dist)
