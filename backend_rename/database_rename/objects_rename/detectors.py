from pupil_apriltags import Detector
from backend_rename.scripts_rename.classes_rename.local_apriltags.LocalFamilyClass import player, house, board


player_detector = Detector(
   families = player.aprltag_family,
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)

house_detector = Detector(
   families = house.aprltag_family,
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)

board_detector = Detector(
   families = board.aprltag_family,
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)