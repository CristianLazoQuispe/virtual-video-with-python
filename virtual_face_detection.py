import virtualvideo

import cv2
import sys

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)



class MyVideoSource(virtualvideo.VideoSource):
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        ret, self.img = self.video_capture.read()
        size = self.img.shape
        #opencv's shape is y,x,channels
        print(size)
        self._size = (size[1],size[0])

    def img_size(self):
        return self._size

    def fps(self):
        return 10

    def generator(self):
        while True:
            ret, frame = self.video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(60, 60)
            )

            for (x, y, w, h) in faces:
                 yield cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            self.img = frame

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

vidsrc = MyVideoSource()
fvd = virtualvideo.FakeVideoDevice()
fvd.init_input(vidsrc)
fvd.init_output(2, 1280, 720, fps=30)
fvd.run()
