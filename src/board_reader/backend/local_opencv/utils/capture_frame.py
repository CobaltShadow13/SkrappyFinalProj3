import config
from src.board_reader.backend.local_opencv.utils.drawing_utilities import CENTER_COLOR, CORNER_COLOR, plot_point, plot_text
import cv2 as cv
import time
from src.board_reader.backend.local_apriltags.LocalDetectionClass import LocalDetection


#### Ben notes of things to add ####
##   - Add a crosshair and tag display to the photo display that is represented. https://blog.fixermark.com/posts/2022/april-tags-python-recognizer/
##   -
##   -

######Capture Frame Function#####
### 9/25/25 4:50 PM; Ben J - this function works by using the open computer vision library. It currently opens the webcam. Takes a frame and converts it to grayscale.
###################  it then uses the detector class to detect the different apriltags_tags in the frame, and print their tag and location to the command line
###################  next steps are going to be figuring out the calibration of the camera. So we should get a board or representation of the physical board ASAP.
###################  figuring out what data is relevant to the positioning of actual objects in the grid. I will probably move on to creating a real representation of
###################  the grid, and researching the division.


def capture_frame(seconds, main_camera, detector):
    cam = main_camera.getCamera()

    frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH)) #Unused for now
    frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT)) #Unused for now


    ret, rawFrame = cam.read() #utilizing the camera 'ret' take a picture and assign it to rawFrame

    ##good practice error check, maybe my camera is off
    if not ret:
        print("Failed process, Exiting Now. Camera is not available.")
        return []

    ##Fix undistort raw image
    frame = rawFrame

    # make the image grayscale for library processing
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #If the camera calibration exists use it, otherwise assign the width over 2 (this is a terrible error check btw)
    h, w = gray.shape[:2]
    fx = main_camera.getfx() if main_camera.getfx() != 0 else w
    fy = main_camera.getfy() if main_camera.getfy() != 0 else w
    cx = main_camera.getcx() if main_camera.getcx() != 0 else w / 2
    cy = main_camera.getcy() if main_camera.getcy() != 0 else h / 2

    # detect tags in the grayscale image
    detections = detector.detect(gray, True, (fx,fy,cx,cy), config.default_tag_size_mm)

    tags = [] #Array of LocalDetections that will be assigned below

#loop that takes all the tags detected in the grayscale frame and draws them with error checking to the terminal. Remove this when porting
    for tag in detections:
        x, y, z = tag.pose_t.flatten()
        print(tag.pose_t.flatten())
        print(f"Detected board tag ID: {tag.tag_id} at {tag.center}, X: {x} Y: {y} Z: {z}")
        tags.append(LocalDetection(tag, None, x, y, z))
        ##draw stuff
        gray = plot_point(gray, tag.center, CENTER_COLOR)
        gray = plot_text(gray, tag.center, CENTER_COLOR, tag.tag_id)
        for corner in tag.corners:
            gray = plot_point(gray, corner, CORNER_COLOR)


    # display the image for debugging
    cv.imshow("AprilTag Detection", gray)

    #time.sleep(30) ##Delay call before returning (remove this for something faster
    # cleanup


    return tags

