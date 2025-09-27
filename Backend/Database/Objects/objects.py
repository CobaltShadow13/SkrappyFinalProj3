from Backend.Scripts.Classes import familyClass, terrainClass

playerTag = familyClass.player.getTagID()
playerTotalSize = familyClass.player.getTotalSize()
playerTagSize = familyClass.player.getTagSize()
playerShape = familyClass.player.getshape()

houseShape = familyClass.house.getshape()
houseTag = familyClass.house.getTagFamily()
houseTotalSize = familyClass.house.getTotalSize()
houseTagSize = familyClass.house.getTagSize()

boardTag = familyClass.board.getTagFamily()
boardTotalSize = familyClass.board.getTotalSize()
boardTagSize = familyClass.board.getTagSize()
boardShape = familyClass.board.getshape()


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
