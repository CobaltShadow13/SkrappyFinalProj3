#Imports
    ## Classes
import sys

from PySide6.QtWidgets import QApplication

from backend.BackendClass import Backend
##Helper Functions

from backend.scripts.utilities.apriltag_utilities.capture_frame import capture_frame
from database.objects.detectors import board_detector
from frontend.scripts.classes.user_interface.main_window_backend_interface import MainWindow



def __main__():
    # Make the grid generalizable later (by that I mean detect the corners for width and height and ask the DM if those are correct, then allow them to change them in the UI

    backend = Backend()

    while True:
        #runs the capture frame every x seconds
        detection_tags = capture_frame(1, backend.get_camera(), board_detector)
        backend.get_board().get_grid().update_grid(detection_tags)

        ##User interface stuff
        app = QApplication(sys.argv)
        window = MainWindow(backend)
        window.show()
        sys.exit(app.exec())

__main__()
