import terrainClass
import familyClass

playerTag = familyClass.player.getTagID()
playerTotalSize = familyClass.player.getTotalSize()
playerTagSize = familyClass.player.getTagSize()
playerShape = familyClass.player.getshape()

house1 = familyClass.house1.getshape()

boardTag = familyClass.board.getTagFamily()
boardTotalSize = familyClass.board.getTotalSize()
boardTagSize = familyClass.board.getTagSize()
boardShape = familyClass.board.getshape()


##board pieces
board0 = terrainClass.BoardPiece('board', boardTag, boardShape, boardTotalSize, boardTagSize, 0)
board1 = terrainClass.BoardPiece('board', boardTag, boardShape, boardTotalSize, boardTagSize, 1)
board2 = terrainClass.BoardPiece('board', boardTag, boardShape, boardTotalSize, boardTagSize, 2)
board3 = terrainClass.BoardPiece('board', boardTag, boardShape, boardTotalSize, boardTagSize,3)


##houses
house0 = terrainClass.BoardPiece('house', familyClass.house.tagID, ( [1,1,1] ,
                                                                                 [1,1,1] ,
                                                                                  [1,1,1] ))
##players
player0 = terrainClass.BoardPiece('board', playerTag, playerShape, playerTotalSize, familyClass.player.tagSize, 0)
player1 = terrainClass.BoardPiece('board', playerTag, playerShape, playerTotalSize, playerTagSize, 1)
player2 = terrainClass.BoardPiece('board', playerTag, playerShape, playerTotalSize, playerTagSize, 2)
player3 = terrainClass.BoardPiece('board', playerTag, playerShape, playerTotalSize, playerTagSize,3)
