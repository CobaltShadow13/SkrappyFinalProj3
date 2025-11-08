#Btoard Piece Class
import config

class BoardPiece(object):
#Constructor
    def __init__(self, name, apriltag_family, shape, tag_num, tag_image): ##Tag image is a file path as a raw string?
        self.name = name
        self.dir = dir
        self.apriltag_family = apriltag_family
        self.tag = self.apriltag_family.assign_tag()
        self.shape = shape
        self.tag_num = tag_num

        ##In the constructor set the tag_image path
        if config.preset == "Chess":
            if self.get_name() == "B_King":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\chess\Chess_kdt60.png"
            elif self.get_name() == "B_Queen":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\chess\Chess_qdt60.png"
            elif self.get_name() == "B_Knight":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\chess\Chess_ndt60.png"
            elif self.get_name() == "B_Rook":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\chess\Chess_rdt60.png"
            elif self.get_name() == "B_Bishop":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\chess\Chess_bdt60.png"
            elif self.get_name() == "B_Pawn":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\chess\Chess_pdt60.png"
            elif self.get_name() == "W_King":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\chess\Chess_klt60.png"
            elif self.get_name() == "W_Queen":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\chess\Chess_qlt60.png"
            elif self.get_name() == "W_Knight":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\chess\Chess_nlt60.png"
            elif self.get_name() == "W_Rook":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\chess\Chess_rlt60.png"
            elif self.get_name() == "W_Bishop":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\chess\Chess_blt60.png"
            elif self.get_name() == "W_Pawn":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\chess\Chess_plt60.png"
            else:
                self.tag_image = tag_image

        elif config.preset == "D&D":
            if self.get_name() == "Player":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\dnd\D&D_Character.png"
            elif self.get_name() == "Enemy":
                self.tag_image = "FILEPATH HERE"
            elif self.get_name() == "Main_Room":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\dnd\DnD_House.png"
            else:
                self.tag_image = tag_image

        elif config.preset == "Monopoly":
            if self.get_name() == "Board":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\monopoly\MonopolyBoard.png"
            elif self.get_name() == "Hat":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\monopoly\MonopolyHatPiece.png"
            else:
                self.tag_image = tag_image
        elif config.preset == "MagicTheGathering":
            if self.get_name() == "Card":
                self.tag_image = "D:\SERAPH_AI\SkrappyFinalProj3\data\display_images\card_game\MTG_Card.jpg"
        else:
            self.tag_image = tag_image ##file path
# Getters
    def get_name(self):
        return self.name
    def get_apriltag_family(self):
        return self.apriltag_family
    def get_shape(self):
        return self.shape
    def get_tag_num(self):
        return self.tag_num
    def get_tag_image(self):
        return self.tag_image

#Setters
    def set_name(self, name):
        self.name = name
    def set_apriltag_family(self, family):
        self.apriltag_family = family
    def set_shape(self, shape):
        self.shape = shape
    def set_tag_num(self, tag_id):
        self.tag_num = tag_id
    def set_tag_image(self, tag_image):
        self.tag_image = tag_image



#Helper Functinos
######################################################################################################################################################################################