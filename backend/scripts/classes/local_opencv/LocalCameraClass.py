import cv2 as cv
import cv2.aruco as aruco
import numpy as np
import glob
#https://calib.io/pages/camera-calibration-pattern-generator

class LocalCamera(object):
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

    def calibrate_camera(self, board_size=(6, 6), square_size=0.015, marker_size=0.0105):
        # Create dictionary and board
        dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
        board = aruco.CharucoBoard(board_size, square_size, marker_size, dictionary)

        all_corners = []
        all_ids = []
        image_size = None

        images = glob.glob("*.jpg")
        if not images:
            raise FileNotFoundError("No calibration images found.")

        for fname in images:
            img = cv.imread(fname)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            corners, ids, _ = aruco.detectMarkers(gray, dictionary)
            if len(corners) > 0:
                _, charuco_corners, charuco_ids = aruco.interpolateCornersCharuco(corners, ids, gray, board)
                if charuco_corners is not None and len(charuco_corners) > 3:
                    all_corners.append(charuco_corners)
                    all_ids.append(charuco_ids)
                    if image_size is None:
                        image_size = gray.shape[::-1]
                    cv.aruco.drawDetectedCornersCharuco(img, charuco_corners, charuco_ids)
                    cv.imshow("Calibration", img)
                    cv.waitKey(200)

        cv.destroyAllWindows()

        ret, mtx, dist, rvecs, tvecs = aruco.calibrateCameraCharuco(
            all_corners, all_ids, board, image_size, None, None
        )

        # Store values just like your current code
        self.setfx(mtx[0, 0])
        self.setfy(mtx[1, 1])
        self.setcx(mtx[0, 2])
        self.setcy(mtx[1, 2])
        self.setdist(dist)

        np.savez("calibration_charuco.npz", mtx=mtx, dist=dist)

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
