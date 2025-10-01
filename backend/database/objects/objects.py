from backend.scripts.classes import LocalFamilyClass, BoardPieceClass

playerTag = familyClass.player.getTagID()
playerTotalSize = familyClass.player.getTotalSize()
playerTagSize = familyClass.player.getTagSize()
playerShape = familyClass.player.get_shape()

houseShape = familyClass.house.get_shape()
houseTag = familyClass.house.getTagFamily()
houseTotalSize = familyClass.house.getTotalSize()
houseTagSize = familyClass.house.getTagSize()

boardTag = familyClass.board.getTagFamily()
boardTotalSize = familyClass.board.getTotalSize()
boardTagSize = familyClass.board.getTagSize()
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
