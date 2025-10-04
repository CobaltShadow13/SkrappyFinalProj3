from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QTableWidgetItem
from backend.scripts.utilities.board_utilities.board_utilities import create_board_piece
from frontend.scripts.classes.user_interface.main_window_class import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, backend):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.backend = backend
        self.ui.create_board_piece_button.clicked.connect(self.on_create_board_piece)
        self.populate_families()
        self.populate_shapes()

    def add_to_bp_list(self, board_piece):
        bptw = self.ui.board_piece_table_widget
        bptw.setRowCount(bptw.rowCount() + 1)
        bptw.setItem(bptw.rowCount()-1, 0, QTableWidgetItem(board_piece.get_name()))
        bptw.setItem(bptw.rowCount()-1, 1, QTableWidgetItem(board_piece.get_apriltag_family().get_tag_family()))
        bptw.setItem(bptw.rowCount()-1, 2, QTableWidgetItem(str(board_piece.get_tag_num())))


    def on_create_board_piece(self):
        name = self.ui.board_piece_name_input.toPlainText()
        apriltag_family = self.ui.apriltag_family_input_box.currentData()
        shape = self.ui.board_piece_shape_input_box.currentText()
        board = self.backend.get_board()
        create_board_piece(board, name, apriltag_family, shape)
        self.add_to_bp_list(board.get_board_piece_array()[-1])



    def populate_families(self): ##adds all tag families in the current board to the options menu
        for fam in self.backend.get_families():
            self.ui.apriltag_family_input_box.addItem(fam.get_tag_family(), fam)

    def populate_shapes(self):
        for shape in self.backend.get_shapes():
            self.ui.board_piece_shape_input_box.addItem(shape.get_name(), shape)






