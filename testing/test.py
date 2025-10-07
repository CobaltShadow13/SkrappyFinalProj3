import cv2
import sys

print("OpenCV version:", cv2.__version__)
print("Python version:", sys.version)
print("Has aruco:", hasattr(cv2, "aruco"))

try:
    import cv2.aruco as aruco
    print("Aruco module path:", aruco.__file__)
    print("Aruco contents:", dir(aruco)[:10])
except Exception as e:
    print("Aruco import error:", e)
