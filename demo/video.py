import cv2 as cv


class Video:

    def __init__(self, path, species, description=""):
        self.path = path
        self.species = species
        self.description = description

    def __str__(self):
        return '"{}": {} ({})'.format(self.path, self.species, self.description)

    def display(self):
        frames = VideoFrames(self)
        for i, frame in enumerate(frames):
            cv.rectangle(frame, (10, 2), (frame.shape[1] - 10, 20), (255, 255, 255), -1)
            cv.putText(frame, str(frames.capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
            cv.putText(frame, self.description, (80, 15),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

            cv.imshow(self.species + ' (Esc to exit)', frame)
            keyboard = cv.waitKey(30)
            if keyboard == 27:
                break


class VideoFrames:

    def __init__(self, video):
        self.video = video
        self.capture = cv.VideoCapture(cv.samples.findFileOrKeep(video.path))

    def __iter__(self):
        """
        You should only have one iterator at a time.
        """

        if not self.capture.isOpened:
            print('Unable to open: ' + self.video.path)
            return

        while True:
            ret, frame = self.capture.read()

            if frame is None:
                self.capture.set(cv.CAP_PROP_POS_FRAMES, 0)
                break

            yield frame
