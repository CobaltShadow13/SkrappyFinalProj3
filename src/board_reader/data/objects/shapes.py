from src.board_reader.backend.board.ShapeClass import Shape

player_shape = Shape("Player Character", [1])
house_shape_3x3 = Shape("3x3 Tile House", ([1, 1, 1],
                                                            [1, 1, 1],
                                                            [1, 1, 1]))
board_shape = Shape("Boundary Square", [1])

shapes = [player_shape, house_shape_3x3, board_shape]
