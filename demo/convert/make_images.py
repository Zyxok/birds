from demo.convert import video
import os
from PIL import Image


def run(videos):
    for vid in videos:
        v = video.VideoFrames(vid)
        path = "resources\\frames\\" + v.video.path[-10:-4]
        try:
            os.mkdir(path)
        except OSError:
            pass

        index = 0
        for frame in v:
            img = Image.fromarray(frame)
            img.save(path + "\\" + str(index) + ".jpg")
            index += 1
