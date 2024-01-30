from ultralytics import YOLO
import cv2
import vlc
import time
import numpy as np
import os

# os.add_dll_directory(r"D:/AI/libvlc.dll")



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
        if 1 in boxes.cls and boxes.conf > 0.7:
            p = vlc.MediaPlayer(r"D:/AI/10egpA.mp3")
            p.play()
            time.sleep(5)

        if 3 in boxes.cls and boxes.conf > 0.7:
            p = vlc.MediaPlayer(r"D:/AI/20egpA.mp3")
            p.play()
            time.sleep(5)

        if 6 in boxes.cls and boxes.conf > 0.7:
            p = vlc.MediaPlayer(r"D:/AI/5egpA.mp3")
            p.play()
            time.sleep(5)
            
        if 2 in boxes.cls and boxes.conf > 0.7:
            p = vlc.MediaPlayer(r"D:/AI/100egpA.mp3")
            p.play()
            time.sleep(5)

        if 4 in boxes.cls and boxes.conf > 0.7:
            p = vlc.MediaPlayer(r"D:/AI/200egpA.mp3")
            p.play()
            time.sleep(5)
            
        if 7 in boxes.cls and boxes.conf > 0.7:
            p = vlc.MediaPlayer(r"D:/AI/50egpA.mp3")
            p.play()
            time.sleep(5)