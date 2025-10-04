from backend.scripts.classes.board.grid.GridClass import initialize_grid

class Board(object):
#Constructor
    def __init__(self, width, height, tile_size):
        self.grid = initialize_grid(width, height, tile_size)
        self.board_piece_array = []
#Getters
    def get_grid(self):
        return self.grid
    def get_board_piece_array(self):
        return self.board_piece_array
#Setters
    def set_grid(self, grid):
        self.grid = grid
    def set_board_piece_array(self, board_piece_array):
        self.board_piece_array = board_piece_array


#Helper Functions
    ##Create New Board Piece
    ##SaveBoard
