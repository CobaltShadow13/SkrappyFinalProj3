from pupil_apriltags import Detector
from Classes import familyClass

player_detector = Detector(
   families = familyClass.player.tagFamily,
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)

house_detector = Detector(
   families = familyClass.house.tagFamily,
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)

board_detector = Detector(
   families = familyClass.board.tagFamily,
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)