#Imports
    ## Classes
import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from src.board_reader.backend.BackendClass import Backend
##Helper Functions

from src.board_reader.backend.local_opencv.utils.capture_frame import capture_frame
from src.board_reader.data.objects.detectors import board_detector
from src.board_reader.frontend.scripts.classes.user_interface.main_window_backend_interface import MainWindow


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
    timer.start(1000)  # every 1000 ms = 1 second

    # Start the Qt event loop (blocks here, but timer keeps running)
    sys.exit(app.exec())

__main__()
