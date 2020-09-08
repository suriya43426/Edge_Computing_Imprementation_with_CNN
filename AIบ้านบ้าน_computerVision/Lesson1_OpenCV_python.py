import cv2

#cap = cv2.VideoCapture('rtsp://101.20.12.2:5050')
cap = cv2.VideoCapture(0)

_, frame = cap.read()

cv2.imshow('frame', frame)

cv2.waitKey()