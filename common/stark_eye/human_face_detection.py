# import libraries
import os
import cv2
import numpy
import imutils
from imutils.video import VideoStream


def human_face_detector(prototxtPath: str, weightsPath: str):
    model = cv2.dnn.readNetFromCaffe(prototxtPath, weightsPath)
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        model.setInput(blob)
        detections = model.forward()
        count = 0
        for i in range(0, detections.shape[2]):
            box = detections[0, 0, i, 3:7] * numpy.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            confidence = detections[0, 0, i, 2]
            if confidence > 0.165:
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                count = count + 1

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    cv2.destroyAllWindows()
    vs.stop()
