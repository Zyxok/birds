from demo.video import Video

PATH = "resources\\" + "data.csv"


def parse_get_videos():
    with open(PATH, 'r') as f:
        lines = f.readlines()

    field_names = lines[0].split(',')
    videos = []
    for raw_file in lines[1:]:
        file_data = raw_file.split(',')
        path = "resources\\" + file_data[0] + ".MP4"

        if file_data[4] != "":
            continue

        videos.append(Video(path, file_data[2]))

    return videos
