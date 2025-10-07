import subprocess
import os
import re

def inch_to_meters(inch):
    return inch / 39.37

def png_to_svg(tag_path):
    main_path = r"D:\SERAPH_AI\SkrappyFinalProj3\database\assets\apriltag-imgs-master\tag_to_svg.py"
    output_svg = r"D:\SERAPH_AI\SkrappyFinalProj3\database\assets\apriltag-imgs-master\tempsvg.svg"

    command = ["python", main_path, tag_path, output_svg, "--size=25.2mm"]
    subprocess.run(command, check=True)
    return output_svg


def convert_to_apriltag_path(base_directory, tag_family, tag_num):
    match = re.match(r"tag(\d+)h(\d+)", tag_family.get_tag_family())
    if not match:
        raise ValueError(f"Invalid tag family: {tag_family.get_tag_family()}")
    tag_bits, hamming = match.groups()
    family_formatted = f"tag{int(tag_bits):02d}_{int(hamming):02d}"
    tag_str = f"{int(tag_num):05d}"
    filename = f"{family_formatted}_{tag_str}.png"
    full_path = os.path.join(base_directory, filename)
    return full_path