#step 1

import cv2

    cap = cv2.VideoCapture('http://192.168.1.178:11653/videostream.cgi?user=admin&pwd=888888')

while True:
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.waitKey(1)