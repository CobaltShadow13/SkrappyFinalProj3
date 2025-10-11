import os
import sys
import numpy as np
import cv2
import cv2.aruco
import json
from typing import Generator, Tuple, Optional
from camera_calibration_library.src.calibration.calibrate import FisheyeCalibrator, PinholeCalibrator

ARUCO_DICT = cv2.aruco.DICT_4X4_50
SQUARES_VERTICALLY = 5
SQUARES_HORIZONTALLY = 5
SQUARE_LENGTH = 0.0254
MARKER_LENGTH = 0.019
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

instaCamFisheye = FisheyeCalibrator(
    ARUCO_DICT, SQUARES_VERTICALLY, SQUARES_HORIZONTALLY, SQUARE_LENGTH, MARKER_LENGTH, 
    calibration_images_dir= os.path.join(CURRENT_PATH,'data\\calibration\\images\\'),
    raw_images_dir= os.path.join(CURRENT_PATH,'..\\data\\raw_images\\descent_1')
    )

instaCamPinhole = PinholeCalibrator(
    ARUCO_DICT, SQUARES_VERTICALLY, SQUARES_HORIZONTALLY, SQUARE_LENGTH, MARKER_LENGTH, 
    calibration_images_dir= os.path.join(CURRENT_PATH,'data\\calibration\\images\\'),
    raw_images_dir= os.path.join(CURRENT_PATH,'../data/raw_images/descent_1')
    )

instaCamFisheye.calibrate()
#instaCamPinhole.calibrate()

instaCamFisheye.export_camera_params_colmap()
#instaCamPinhole.export_camera_params_colmap()