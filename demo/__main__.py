import demo
import os
import cv2

if not os.path.isdir(".\\demo"):
    raise IOError("This should be run from the \\birds directory.")

for video in demo.json_parser.parse_get_videos():
    print(video)
    video.display()