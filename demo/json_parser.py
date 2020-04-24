import json
from demo.video import Video

JSON_PATH = "resources\\" + "video_data.json"


def parse_get_videos():
    with open(JSON_PATH, 'r') as json_file:
        data = json.loads(json_file.read())

    videos = []
    for file in data:
        path = "resources\\" + file["file"] + file["extension"]
        description = ""
        if "description" in file:
            description = file["description"]
        videos.append(Video(path, file["species"], description))

    return videos


