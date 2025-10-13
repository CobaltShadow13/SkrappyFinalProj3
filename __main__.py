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

    def update_and_refresh():
        frame = capture_frame(1, backend.get_camera(), board_detector)
        backend.get_board().get_grid().update_grid(frame)
        window.refresh_ui_grid()  # <-- update UI after backend changes


    # Timer to periodically run capture_frame and update grid
    timer = QTimer()
    timer.timeout.connect(lambda:(
        update_and_refresh()
    ))
    timer.start(1000)  # every 1000 ms = 1 second



    timer.timeout.connect(update_and_refresh)
    # Start the Qt event loop (blocks here, but timer keeps running)
    sys.exit(app.exec())

__main__()
