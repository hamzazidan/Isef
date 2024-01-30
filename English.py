from ultralytics import YOLO
import cv2
import vlc
import time
import numpy as np


model = YOLO(r"D:/AI/last.pt")
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    results = model(frame, show=True)
    # cv2.imshow('0', results)
    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break

    for result in results:
        boxes = result.boxes.cpu().numpy()
        print(boxes.cls)
        print(boxes.conf)

        if 1 in boxes.cls:
            p = vlc.MediaPlayer(r"D:/AI/10egp.mp3")
            p.play()
            time.sleep(5)

        if 3 in boxes.cls :
            p = vlc.MediaPlayer(r"D:/AI/20egp.mp3")
            p.play()
            time.sleep(5)

        if 6 in boxes.cls :
            p = vlc.MediaPlayer(r"D:/AI/5egp.mp3")
            p.play()
            time.sleep(5)

        if 2 in boxes.cls:
            p = vlc.MediaPlayer(r"D:/AI/100egp.mp3")
            p.play()
            time.sleep(5)

        if 4 in boxes.cls:
            p = vlc.MediaPlayer(r"D:/AI/200egp.mp3")
            p.play()
            time.sleep(5)

        if 7 in boxes.cls:
            p = vlc.MediaPlayer(r"D:/AI/50egp.mp3")
            p.play()
            time.sleep(5)