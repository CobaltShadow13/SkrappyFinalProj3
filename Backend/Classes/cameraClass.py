import cv2 as cv
import numpy as np
import glob


class Camera(object):
    def __init__(self, camera, fx = None, fy = None, cx = None, cy = None, dist = None):
        self.camera = camera
        self.fx = fx
        self.fy = fy
        self.cx = cx
        self.cy = cy
        self.dist = dist

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

    def calibrateCamera(self, pattern_size=(24, 24)):
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points
        square_size = 0.0254
        objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
        objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2) * square_size

        objpoints = []  # 3d points
        imgpoints = []  # 2d points

        images = glob.glob('*.jpg')
        if not images:
            raise FileNotFoundError("No calibration images found.")

        for fname in images:
            img = cv.imread(fname)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            ret, corners = cv.findChessboardCorners(gray, pattern_size, None)
            if ret:
                objpoints.append(objp)
                corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                imgpoints.append(corners2)

                cv.drawChessboardCorners(img, pattern_size, corners2, ret)
                cv.imshow('Calibration', img)
                cv.waitKey(250)

        cv.destroyAllWindows()

        # calibrate
        ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

        # update class values
        self.setfx(mtx[0, 0])
        self.setfy(mtx[1, 1])
        self.setcx(mtx[0, 2])
        self.setcy(mtx[1, 2])
        self.setdist(dist)

        np.savez("calibration.npz", mtx=mtx, dist=dist)

        return mtx, dist, rvecs, tvecs

    def undistortImage(self, img):
        h, w = img.shape[:2]
        mtx = self.getCameraMatrix()
        newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, self.dist, (w, h), 1, (w, h))
        return cv.undistort(img, mtx, self.dist, None, newcameramtx)

    def loadCalibration(self, filename):
        data = np.load(filename)
        mtx, dist = data["mtx"], data["dist"]
        self.setfx(mtx[0, 0])
        self.setfy(mtx[1, 1])
        self.setcx(mtx[0, 2])
        self.setcy(mtx[1, 2])
        self.setdist(dist)
