import cv2 as cv
import numpy

class Video:

    def __init__(self, path, species):
        self.path = path
        self.species = species

    def __str__(self):
        return '"{}": {}'.format(self.path, self.species)

    def display(self):
        frames = VideoFrames(self)
        for frame in frames:
            #cv.rectangle(frame, (10, 2), (frame.shape[1] - 10, 20), (255, 255, 255), -1)
            #cv.putText(frame, str(frames.capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
            #           cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
            # cv.putText(frame, "", (80, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

            cv.imshow(self.species + ' (Esc to exit)', frame)
            keyboard = cv.waitKey(30)
            if keyboard == 27:
                break

    def dimensions(self):
        frames = VideoFrames(self)
        for frame in frames:
            return frame.shape


class VideoFrames:
    def __init__(self, video):
        self.video = video
        self.capture = cv.VideoCapture(cv.samples.findFileOrKeep(video.path))

    def __iter__(self):
        """
        You should only have one iterator at a time per instance.
        """

        if not self.capture.isOpened:
            print('Unable to open: ' + self.video.path)
            return

        while True:
            frame: numpy.ndarray

            ret, frame = self.capture.read()

            if frame is None:
                self.capture.set(cv.CAP_PROP_POS_FRAMES, 0)
                break

            # Resizing and cropping

            if frame.shape[0] != 360 or frame.shape[1] != 640:
                frame = cv.resize(frame, dsize=(640, 360),
                                  interpolation=cv.INTER_AREA)
            frame = frame[:, 55:, :]
            # 360 by 585
            yield frame
