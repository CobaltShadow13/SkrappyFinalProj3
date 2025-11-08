import time
from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
import ast
import config
from src.board_reader.backend.board.ShapeClass import Shape
from src.board_reader.backend.board.utils.board_utilities import create_board_piece
from src.board_reader.backend.utils.conversions import convert_to_apriltag_path, png_to_svg
from src.board_reader.frontend.scripts.classes.user_interface.main_window_class import Ui_MainWindow
from PySide6.QtCore import Qt
import os
from PySide6.QtCore import QPointF, QRectF
from PySide6.QtGui import QPixmap, Qt, QPen, QColor, QPainter
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem


class BoardGraphicsView(QGraphicsView):
    def __init__(self, backend, tile_size=64, parent=None):
        super().__init__(parent)
        self.backend = backend
        self.tile_size = tile_size
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setRenderHints(self.renderHints() | QPainter.RenderHint.SmoothPixmapTransform)
        self.setBackgroundBrush(QColor(30, 30, 30))
        self.piece_items = {}

    def draw_grid(self):
        grid = self.backend.get_board().get_grid()
        rows = int(grid.get_height())
        cols = int(grid.get_width())

        pen = QPen(QColor(80, 80, 80))
        for r in range(rows + 1):
            self.scene.addLine(0, r * self.tile_size, cols * self.tile_size, r * self.tile_size, pen)
        for c in range(cols + 1):
            self.scene.addLine(c * self.tile_size, 0, c * self.tile_size, rows * self.tile_size, pen)

        self.setSceneRect(QRectF(0, 0, cols * self.tile_size, rows * self.tile_size))

    def refresh_scene(self):
        # Clear old piece drawings
        for item in list(self.piece_items.values()):
            self.scene.removeItem(item)
        self.piece_items.clear()

        grid = self.backend.get_board().get_grid()

        for tile in grid.get_tile_map():
            board_piece = getattr(tile, "get_current_board_piece", lambda: None)()
            if not board_piece:
                continue

            if board_piece in self.piece_items:
                old_item = self.piece_items.pop(board_piece)
                self.scene.removeItem(old_item)

            image_path = getattr(board_piece, "get_tag_image", lambda: None)()
            if not image_path or not os.path.exists(image_path):
                continue

            shape = getattr(board_piece, "get_shape", lambda: None)()
            width_tiles, height_tiles = 1, 1

            # --- New: Support ShapeMatrix ---
            if shape:
                if hasattr(shape, "shape_matrix"):
                    matrix = shape.get_shape()
                    height_tiles = len(matrix)
                    width_tiles = max(len(row) for row in matrix) if height_tiles > 0 else 1
                else:
                    # Fallback to existing methods if available
                    width_tiles = getattr(shape, "get_width", lambda: 1)()
                    height_tiles = getattr(shape, "get_height", lambda: 1)()

            # Determine pixel position
            tile_id = tile.get_tile_id()
            row, col = self._tile_id_to_coords(tile_id)
            x = col * self.tile_size
            y = row * self.tile_size

            # Scale image according to shape
            pixmap = QPixmap(image_path).scaled(
                self.tile_size * width_tiles,
                self.tile_size * height_tiles,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

            pix_item = QGraphicsPixmapItem(pixmap)
            pix_item.setPos(QPointF(x, y))
            pix_item.setZValue(1)
            self.scene.addItem(pix_item)
            self.piece_items[board_piece] = pix_item

    def _tile_id_to_coords(self, tile_id):
        width = self.backend.get_board().get_grid().get_width()
        col = int(tile_id / width)
        row_bottom_up = tile_id % width
        row = (width - 1) - row_bottom_up
        return row, col

class TileTableWidgetItem(QTableWidgetItem):
    def __init__(self, tile):
        super().__init__()
        #self.setText(f"{int(tile.get_has_tag())}")
        self.setText(f"{tile.get_x_meter_coord(), tile.get_y_meter_coord()}")
        self.tile = tile
    def get_tile(self):
        return self.tile

class BoardPieceWidgetItem(QTableWidgetItem):
    def __init__(self, board_piece):
        super().__init__()
        self.board_piece = board_piece
        self.setText("Print?")
        self.setBackground(QtGui.QColor(0,0,0))
    def get_board_piece(self):
        return self.board_piece

class MainWindow(QMainWindow):
    def __init__(self, backend):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.backend = backend
        # --- Create a graphics view to visualize the board ---
        self.board_graphics_view = BoardGraphicsView(self.backend, tile_size=64)
        self.board_graphics_view.draw_grid()

        # Add it to your existing layout (replace if you have a placeholder)
        if hasattr(self.ui, "board_grid_container_layout"):
            self.ui.board_grid_container_layout.addWidget(self.board_graphics_view)
        else:
            # fallback: just show it floating for now
            self.board_graphics_view.show()
        self.ui.create_board_piece_button.clicked.connect(self.on_create_board_piece)
        self.populate_families()


    def add_to_bp_list(self, board_piece):
        bptw = self.ui.board_piece_table_widget
        tile_link_widget = BoardPieceWidgetItem(board_piece)
        bptw.setRowCount(bptw.rowCount() + 1)
        bptw.setItem(bptw.rowCount()-1, 0, QTableWidgetItem(board_piece.get_name()))
        bptw.setItem(bptw.rowCount()-1, 1, QTableWidgetItem(board_piece.get_apriltag_family().get_tag_family()))
        bptw.setItem(bptw.rowCount()-1, 2, QTableWidgetItem(str(board_piece.get_tag_num())))
        bptw.setItem(bptw.rowCount()-1, 3, tile_link_widget)


    def on_create_board_piece(self):
        name = self.ui.board_piece_name_input.toPlainText()
        apriltag_family = self.ui.apriltag_family_input_box.currentData()
        shape_name = self.ui.board_piece_shape_input.toPlainText()
        shape_matrix = ast.literal_eval(f"{self.ui.board_piece_matrix_input.toPlainText()}")
        shape = Shape(shape_name, shape_matrix)
        board = self.backend.get_board()
        image_path = self.ui.board_piece_image_path_input_2.toPlainText()
        create_board_piece(board, name, apriltag_family, shape, image_path)
        self.add_to_bp_list(board.get_board_piece_array()[-1])

    def populate_families(self): ##adds all tag families in the current board to the options menu
        for fam in self.backend.get_families():
            self.ui.apriltag_family_input_box.addItem(fam.get_tag_family(), fam)

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


    def refresh_ui_grid(self):
        print("=== REFRESH GRAPHICS START ===")
        self.board_graphics_view.refresh_scene()

    def print_tag(self, board_piece):
        tag_family_string = board_piece.get_apriltag_family().get_tag_family()

        base_dir = config.base_family_dir
        full_path = os.path.join(base_dir, tag_family_string)
        tag_path = convert_to_apriltag_path(full_path, board_piece.get_apriltag_family(), board_piece.get_tag_num())
        svg_path = png_to_svg(tag_path)
        os.startfile(svg_path)  # Windows default printer action
        time.sleep(2)
        os.remove(svg_path)











