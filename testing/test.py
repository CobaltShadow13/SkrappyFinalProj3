import cv2 as cv
import glob


def detect_board_settings(image_folder, candidate_boards):
    """
    Tries different dictionary + board size combinations to find one that produces ChArUco corners.

    image_folder: folder containing calibration data
    candidate_boards: list of tuples (dictionary_name, squaresX, squaresY)
    """
    images = glob.glob(f"{image_folder}/*.jpg")
    if not images:
        raise FileNotFoundError("No data found in folder.")

    print(f"🔍 Found {len(images)} data for testing.")

    for dict_name, squaresX, squaresY in candidate_boards:
        try:
            dictionary = getattr(cv.aruco, f"DICT_{dict_name}")
            aruco_dict = cv.aruco.getPredefinedDictionary(dictionary)
            board = cv.aruco.CharucoBoard(
                (squaresX, squaresY),  # squaresX, squaresY
                0.015,  # squareLength in meters
                0.011,  # markerLength in meters
                aruco_dict
            )
            print(f"\nTesting board: {dict_name}, size: {squaresX}x{squaresY}")

            for fname in images[:5]:  # test on first 5 data
                img = cv.imread(fname)
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                corners, ids, _ = cv.aruco.detectMarkers(gray, aruco_dict)

                if ids is not None and len(ids) > 0:
                    retval, charuco_corners, charuco_ids = cv.aruco.interpolateCornersCharuco(
                        corners, ids, gray, board
                    )
                    print(
                        f"{fname} -> retval: {retval}, corners: {0 if charuco_corners is None else len(charuco_corners)}")
                else:
                    print(f"{fname} -> No markers detected")

        except Exception as e:
            print(f"Error testing board {dict_name} {squaresX}x{squaresY}: {e}")


# Example usage
candidate_boards = [
    ("4X4_50", 6, 6),
    ("4X4_50", 5, 7),
    ("5X5_100", 6, 6),
    ("5X5_100", 5, 7),
    ("6X6_50", 6, 6),
]

detect_board_settings(r"D:\SERAPH_AI\SkrappyFinalProj3\database\assets\calibration_images", candidate_boards)
