from demo.convert.video import Video

PATH = "resources\\" + "data_condensed.csv"


def parse_get_videos():
    videos = []
    with open(PATH, 'r') as f:
        for line in f.readlines():
            path, species = line.rstrip().split(',')
            videos.append(Video(path, species))

    return videos
