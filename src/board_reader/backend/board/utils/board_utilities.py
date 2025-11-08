#####How do we capture shapes???
from src.board_reader.backend.board.BoardClass import Board
from src.board_reader.backend.board.BoardPieceClass import BoardPiece


def create_board(width, height, tile_size):
    new_board = Board(width, height, tile_size)
    return new_board

def create_board_piece(board, name, apriltag_family, shape, image_path):
    new_board_piece = BoardPiece(name, apriltag_family, shape, apriltag_family.get_assigned_tags_num(), image_path)
    board.get_board_piece_array().append(new_board_piece)

def draw_shape():
    pass #working on?