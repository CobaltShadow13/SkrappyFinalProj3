#Imports
    ## Classes
import sys
from PySide6.QtCore import QTimer #import the timer module
from PySide6.QtWidgets import QApplication #import the main frontend Class
from src.board_reader.backend.BackendClass import Backend #Import the backend.
    ## Helper Functions
from src.board_reader.backend.local_opencv.utils.capture_frame import capture_frame #import the capture frame helper function
from src.board_reader.frontend.scripts.classes.user_interface.main_window_backend_interface import MainWindow #Import the main window subclass
    ## Objects
from src.board_reader.data.objects.detectors import board_detector #Import the "Board Detector" object from the data file

def __main__():
    backend = Backend()#Initialize the backend object and assign it to the variable 'backend' this is created using the variables in config

    # User interface setup
    app = QApplication(sys.argv) #Create new user interface
    window = MainWindow(backend) #Create the main window subclass object using the backend object created above
    window.show() #Show the main window

    def update_and_refresh():
        frame = capture_frame(1, backend.get_camera(), board_detector) #Frame is an array of tags that is returned from the apriltag detection
        backend.get_board().get_grid().update_grid(frame, backend.get_board().get_board_piece_array()) #run the update grid function on grid using the above array of tags 'Frame'
        window.refresh_ui_grid()  # <-- update UI after backend changes


    # Timer to periodically run capture_frame and update grid
    timer = QTimer()#Qtimer from PySide6

    timer.timeout.connect(lambda:(
        update_and_refresh()
    )) #syntax for the timer to function
    timer.start(1000)  # run every 1000 ms

    timer.timeout.connect(update_and_refresh) #On timer run connect the update and refresh function

    sys.exit(app.exec()) #Exit if the exit button is hit.

__main__()
