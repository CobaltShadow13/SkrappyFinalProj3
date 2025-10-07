import cv2 as cv
import numpy as np
import glob
import os
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

    def calibrate_camera(self, image_folder=r"D:\SERAPH_AI\SkrappyFinalProj3\database\assets\calibration_images"):


        # --- Create ArUco dictionary and ChArUco board ---
        dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_50)
        board = cv.aruco.CharucoBoard(
            (6, 6),  # squaresX, squaresY
            0.015,  # squareLength in meters
            0.011,  # markerLength in meters
            dictionary
        )

        aruco_detector = cv.aruco.ArucoDetector(dictionary)

        all_charuco_corners = []
        all_charuco_ids = []
        image_size = None

        # --- Load images ---
        images = glob.glob(os.path.join(image_folder, "*.jpg"))
        if not images:
            raise FileNotFoundError(f"No images found in folder: {image_folder}")
        print(f"🔍 Found {len(images)} calibration images.")

        for idx, fname in enumerate(images):
            img = cv.imread(fname)
            if img is None:
                print(f"Could not read image: {fname}")
                continue

            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            corners, ids, _ = aruco_detector.detectMarkers(gray)

            img_markers = img.copy()
            cv.aruco.drawDetectedMarkers(img_markers, corners, ids)

            for i, c in enumerate(corners):
                print(f"Marker {ids[i][0]} corners:\n{c}")
            if ids is not None:
                print("Detected marker IDs:", ids.flatten())
            cv.imshow("ArUco Detection", img_markers)
            cv.waitKey(500)

            if ids is not None and len(ids) > 0:
                # Interpolate ChArUco corners
                retval, charuco_corners, charuco_ids = cv.aruco.interpolateCornersCharuco(
                    markerCorners=corners,
                    markerIds=ids,
                    image=gray,
                    board=board
                )
                print("retval:", retval, "charuco_corners:", charuco_corners, "charuco_ids:", charuco_ids)
                print(f"Detected markers: {ids}, ChArUco corners: {charuco_corners}")
                if retval is not None and retval > 3:
                    print(f"Appending {retval} corners:", charuco_corners.flatten())
                    all_charuco_corners.append(charuco_corners)
                    all_charuco_ids.append(charuco_ids)
                if retval > 0:  # Need at least 4 corners
                    all_charuco_corners.append(charuco_corners)
                    all_charuco_ids.append(charuco_ids)
                    if image_size is None:
                        image_size = gray.shape[::-1]

                    # Visualization
                    cv.aruco.drawDetectedMarkers(img, corners, ids)
                    cv.aruco.drawDetectedCornersCharuco(img, charuco_corners, charuco_ids)
                    cv.imshow("ChArUco Calibration", img)
                    print("Detected marker IDs:", ids.flatten())
                    cv.waitKey(200)

                    print(
                        f"✅ Processed image {idx + 1}/{len(images)}: {os.path.basename(fname)} - {len(charuco_ids)} corners")
                else:
                    print(f"Not enough ChArUco corners in image: {fname}")
            else:
                print(f"No markers detected in image: {fname}")

        cv.destroyAllWindows()

        if not all_charuco_corners:
            raise RuntimeError("No ChArUco corners detected. Check lighting, focus, and dictionary.")

        # --- Calibrate camera ---
        ret, mtx, dist, rvecs, tvecs = cv.aruco.calibrateCameraCharuco(
            charucoCorners=all_charuco_corners,
            charucoIds=all_charuco_ids,
            board=board,
            imageSize=image_size,
            cameraMatrix=None,
            distCoeffs=None
        )

        # --- Store results in your object ---
        self.setfx(mtx[0, 0])
        self.setfy(mtx[1, 1])
        self.setcx(mtx[0, 2])
        self.setcy(mtx[1, 2])
        self.setdist(dist)

        # --- Save calibration ---
        np.savez("calibration_charuco.npz", mtx=mtx, dist=dist)

        print("\nChArUco Calibration complete")
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
