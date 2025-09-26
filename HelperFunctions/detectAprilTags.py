from Objects.detectors import board_detector
import cv2 as cv
import time

#### Ben notes of things to add ####
##   - Add a crosshair and tag display to the photo display that is represented. https://blog.fixermark.com/posts/2022/april-tags-python-recognizer/
##   -
##   -

######Capture Frame Function#####
### 9/25/25 4:50 PM; Ben J - this function works by using the open computer vision library. It currently opens the webcam. Takes a frame and converts it to grayscale.
###################  it then uses the detector class to detect the different apriltags in the frame, and print their tag and location to the command line
###################  next steps are going to be figuring out the calibration of the camera. So we should get a board or representation of the physical board ASAP.
###################  figuring out what data is relevant to the positioning of actual objects in the grid. I will probably move on to creating a real representation of
###################  the grid, and researching the division.


def captureframe(seconds, mainCamera):
    cam = mainCamera.getCamera()

    frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))
    ret, rawFrame = cam.read()

    ##good practice error check, maybe my camera is off
    if not ret:
        print("Failed process, Exiting Now")
        return 0
##Fix undistort raw image sometime soon
    frame = rawFrame

    # make the image grayscale for library processing
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detect tags in the grayscale image
    detections = board_detector.detect(gray, True, (mainCamera.getfy(), mainCamera.getfy(), mainCamera.getcx(), mainCamera.getcy()))

#loop that takes all the tags detected in the grayscale frame and will later be used to return frame data to the map
    for tag in detections:
        print(f"Detected board tag ID: {tag.tag_id} at {tag.center}")


    # display the image
    cv.imshow("AprilTag Detection", gray)

    # exit using the q key
    if cv.waitKey(1) & 0xFF == ord('q'):
        return 1

    #delay time before ending the function call allows optimization

    time.sleep(seconds)
    # cleanup
    cam.release()
    cv.destroyAllWindows()

    return 0

