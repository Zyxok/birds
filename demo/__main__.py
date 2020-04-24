import demo.json_parser
import os

if not os.path.isdir(".\\demo"):
    raise IOError("This should be run from the \\birds directory.")

# for video in demo.json_parser.parse_get_videos():

video_robin_shortened = demo.json_parser.parse_get_videos()[1]
print(video_robin_shortened)
video_robin_shortened.display()
