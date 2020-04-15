import cv2


class Video:

    def __init__(self, path):
        self.path = path

    def display(self):
        capture = cv2.VideoCapture(cv2.samples.findFileOrKeep(self.path))

        if not capture.isOpened:
            print('Unable to open: ' + self.path)
            return

        while True:
            ret, frame = capture.read()
            if frame is None:
                break

            cv2.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
            cv2.putText(frame, str(capture.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

            cv2.imshow('Frame', frame)

            keyboard = cv2.waitKey(30)
            if keyboard == 'q' or keyboard == 27:
                break
