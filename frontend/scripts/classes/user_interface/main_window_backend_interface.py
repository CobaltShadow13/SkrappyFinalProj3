
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton

from backend.scripts.utilities.board_utilities.board_utilities import create_board_piece
from frontend.scripts.classes.user_interface.main_window_class import Ui_MainWindow
from backend.BackendClass import Backend


class MainWindow(QMainWindow):
    def __init__(self, backend):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.backend = backend
        self.ui.create_board_piece_button.clicked.connect(self.on_create_board_piece)
        self.add_families()

    def on_create_board_piece(self):
        name = self.ui.board_piece_name_input.toPlainText()
        apriltag_family = self.ui.apriltag_family_input_box.currentData()
        shape = self.ui.board_piece_shape_input_box.currentText()
        board = self.backend.get_board()
        create_board_piece(board, name, apriltag_family, shape)

    def add_families(self): ##adds all tag families in the current board to the options menu
        for fam in self.backend.get_families():
            self.ui.apriltag_family_input_box.addItem(fam.get_tag_family(), fam)

    def add_




