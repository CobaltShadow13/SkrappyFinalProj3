playerTag = familyClass.player.get_tag_id()
playerTotalSize = familyClass.player.get_total_size()
playerTagSize = familyClass.player.get_tag_size()
playerShape = familyClass.player.get_shape()

houseShape = familyClass.house.get_shape()
houseTag = familyClass.house.get_tag_family()
houseTotalSize = familyClass.house.get_total_size()
houseTagSize = familyClass.house.get_tag_size()

boardTag = familyClass.board.get_tag_family()
boardTotalSize = familyClass.board.get_total_size()
boardTagSize = familyClass.board.get_tag_size()
boardShape = familyClass.board.get_shape()


##board pieces
board0 = terrainClass.BoardPiece('board', boardTag, boardShape, boardTotalSize, boardTagSize, 0)
board1 = terrainClass.BoardPiece('board', boardTag, boardShape, boardTotalSize, boardTagSize, 1)
board2 = terrainClass.BoardPiece('board', boardTag, boardShape, boardTotalSize, boardTagSize, 2)
board3 = terrainClass.BoardPiece('board', boardTag, boardShape, boardTotalSize, boardTagSize, 3)


##houses
house0 = terrainClass.BoardPiece('house', houseTag, houseShape, houseTotalSize, houseTagSize, 0)


##players
player0 = terrainClass.BoardPiece('board', playerTag, playerShape, playerTotalSize, familyClass.player.tagSize, 0)
player1 = terrainClass.BoardPiece('board', playerTag, playerShape, playerTotalSize, playerTagSize, 1)
player2 = terrainClass.BoardPiece('board', playerTag, playerShape, playerTotalSize, playerTagSize, 2)
player3 = terrainClass.BoardPiece('board', playerTag, playerShape, playerTotalSize, playerTagSize, 3)
