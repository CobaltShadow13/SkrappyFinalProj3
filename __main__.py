#Imports
    ## Classes
import sys
import keyboard
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from backend.BackendClass import Backend
##Helper Functions

from backend.scripts.utilities.apriltag_utilities.capture_frame import capture_frame
from database.objects.detectors import board_detector
from frontend.scripts.classes.user_interface.main_window_backend_interface import MainWindow


def __main__():
    backend = Backend()
    # User interface setup
    app = QApplication(sys.argv)
    window = MainWindow(backend)
    window.show()

    # Timer to periodically run capture_frame and update grid
    timer = QTimer()
    timer.timeout.connect(lambda: backend.get_board().get_grid().update_grid(
        capture_frame(1, backend.get_camera(), board_detector)
    ))
    timer.start(30000)  # every 1000 ms = 1 second

    # Start the Qt event loop (blocks here, but timer keeps running)
    sys.exit(app.exec())

__main__()
