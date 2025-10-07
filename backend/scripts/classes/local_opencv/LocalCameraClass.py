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

    def calibrate_camera(self, board_size=(6, 6), square_size=0.025, marker_size=0.0178):
        # --- Create the dictionary and ChArUco board ---
        dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_100)
        board = cv.aruco.CharucoBoard(board_size, square_size, marker_size, dictionary)

        # --- Initialize the new API detector objects ---
        aruco_params = cv.aruco.DetectorParameters()
        aruco_detector = cv.aruco.ArucoDetector(dictionary, aruco_params)
        charuco_detector = cv.aruco.CharucoDetector(board)

        all_corners = []
        all_ids = []
        image_size = None

        # --- Load calibration images ---
        images = glob.glob(r"D:\SERAPH_AI\SkrappyFinalProj3\database\assets\calibration_images\*.jpg")
        if not images:
            raise FileNotFoundError("No calibration images found at the given path.")

        print(f"Found {len(images)} calibration images.")

        for fname in images:
            img = cv.imread(fname)
            if img is None:
                print(f"⚠️ Skipping unreadable file: {fname}")
                continue

            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            gray = cv.equalizeHist(gray)

            # --- Detect ArUco markers ---
            corners, ids, rejected = aruco_detector.detectMarkers(gray)

            if ids is not None and len(ids) > 0:
                # --- Detect ChArUco corners (new API: returns only 2 values) ---
                charuco_corners, charuco_ids = charuco_detector.detectBoard(gray)

                if charuco_corners is not None and len(charuco_corners) > 3:
                    all_corners.append(charuco_corners)
                    all_ids.append(charuco_ids)

                    if image_size is None:
                        image_size = gray.shape[::-1]

                    # Draw detections
                    cv.aruco.drawDetectedMarkers(img, corners, ids)
                    cv.aruco.drawDetectedCornersCharuco(img, charuco_corners, charuco_ids)
                    cv.imshow("Calibration", img)
                    cv.waitKey(200)
                else:
                    print(f"⚠️ No ChArUco corners found in {fname}")
            else:
                print(f"⚠️ No ArUco markers detected in {fname}")

        cv.destroyAllWindows()

        if not all_corners:
            raise RuntimeError("No ChArUco corners were detected. Check lighting and board visibility.")

        # --- Calibrate camera ---
        ret, mtx, dist, rvecs, tvecs = cv.aruco.calibrateCameraCharuco(
            charucoCorners=all_corners,
            charucoIds=all_ids,
            board=board,
            imageSize=image_size,
            cameraMatrix=None,
            distCoeffs=None
        )

        # --- Store calibration parameters ---
        self.setfx(mtx[0, 0])
        self.setfy(mtx[1, 1])
        self.setcx(mtx[0, 2])
        self.setcy(mtx[1, 2])
        self.setdist(dist)

        np.savez("calibration_charuco.npz", mtx=mtx, dist=dist)

        print("✅ Calibration complete!")
        print("RMS error:", ret)
        print("Camera matrix:\n", mtx)
        print("Distortion coefficients:\n", dist)

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
