from PyQt6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QTableWidgetItem, QTableWidget, QHeaderView
from backend.scripts.utilities.board_utilities.board_utilities import create_board_piece
from frontend.scripts.classes.user_interface.main_window_class import Ui_MainWindow


class TileTableWidgetItem(QTableWidgetItem):
    def __init__(self, tile):
        super().__init__()
        self.setText(f"(({int(tile.get_x_tile_coord())}, {int(tile.get_y_tile_coord())})")
        self.tile = tile
    def get_tile(self):
        return self.tile

class MainWindow(QMainWindow):
    def __init__(self, backend):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.backend = backend
        self.ui.create_board_piece_button.clicked.connect(self.on_create_board_piece)
        self.populate_families()
        self.populate_shapes()
        self.populate_ui_grid()

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

    def transfer_tile_id_to_table_widget_coords(self, tile_id):
        width = self.backend.get_board().get_grid().get_width()
        col = tile_id / width
        row_bottom_up = tile_id % width
        row = (width - 1) - row_bottom_up

        return row, col

    def make_cells_square(self, table):
        table_width = table.viewport().width()
        table_height = table.viewport().height()

        cell_width = table_width / table.columnCount()
        cell_height = table_height / table.rowCount()
        side = min(cell_width, cell_height)

        for x in range(table.columnCount()):
            table.setColumnWidth(x, side)
        for y in range(table.rowCount()):
            table.setRowHeight(y, side)

    def populate_ui_grid(self):
        bgtw = self.ui.board_grid_table_widget
        width = self.backend.get_board().get_grid().get_width()
        height = self.backend.get_board().get_grid().get_height()
        bgtw.setRowCount(height)
        bgtw.setColumnCount(width)


        tile_widgets = []
        for tile in self.backend.get_board().get_grid().get_tile_map():
            tile_widgets.append(TileTableWidgetItem(tile))
        for tile_widget in tile_widgets:
            tile_id = tile_widget.get_tile().get_tile_id()
            row, col = self.transfer_tile_id_to_table_widget_coords(tile_id)
            bgtw.setItem(row, col, tile_widget)
        bgtw.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        bgtw.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.make_cells_square(bgtw)









