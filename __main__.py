#Imports
    ## Classes
import sys

from PySide6.QtWidgets import QApplication

from backend.BackendClass import Backend
from backend.scripts.classes.local_opencv.LocalCameraClass import LocalCamera
from backend.scripts.classes.board.grid.GridClass import initialize_grid
    ##Helper Functions
from backend.scripts.utilities.apriltag_utilities.capture_frame import capture_frame
from backend.scripts.utilities.general_utilities.conversions import inch_to_meters
from backend.database.objects.detectors import board_detector
from frontend.user_interface.main_window_backend_interface import MainWindow



def __main__():
    # Make the grid generalizable later (by that I mean detect the corners for width and height and ask the DM if those are correct, then allow them to change them in the UI

    backend = Backend()

    while True:
        #runs the capture frame every x seconds
        detection_tags = capture_frame(1, backend.get_camera(), board_detector)
        backend.get_board().get_grid().update_grid(detection_tags)

        ##User interface stuff
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())

__main__()
