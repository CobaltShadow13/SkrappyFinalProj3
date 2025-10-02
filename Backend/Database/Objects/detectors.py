from pupil_apriltags import Detector
from backend.scripts.classes.LocalFamilyClass import LocalFamily, player, house, board


player_detector = Detector(
   families = player.tagFamily,
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)

house_detector = Detector(
   families = house.tagFamily,
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)

board_detector = Detector(
   families = board.tagFamily,
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)