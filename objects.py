import terrainClass
import familyClass


##board pieces
board0 = terrainClass.BoardPiece('board', familyClass.player.tagID, [1], 0)
board1 = terrainClass.BoardPiece('board', familyClass.player.tagID,[1], 1)
board2 = terrainClass.BoardPiece('board', familyClass.player.tagID,[1], 2)
board3 = terrainClass.BoardPiece('board', familyClass.player.tagID,[1],3)


##houses
house0 = terrainClass.BoardPiece('house', familyClass.house.tagID, ( [1,1,1] ,
                                                                   [1,1,1] ,
                                                                   [1,1,1] ), 0)
##players
player0 = terrainClass.BoardPiece('player', familyClass.player.tagID, [1], 0)
player1 = terrainClass.BoardPiece('player', familyClass.player.tagID, [1], 1)
player2 = terrainClass.BoardPiece('player', familyClass.player.tagID, [1], 2)
player3 = terrainClass.BoardPiece('player', familyClass.player.tagID, [1], 3)
