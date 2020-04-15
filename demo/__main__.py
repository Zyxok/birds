import demo.json_parser

for video in demo.json_parser.get_videos():
    print(video)
    video.display()