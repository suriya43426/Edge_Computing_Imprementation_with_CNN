import cv2
import numpy as np
import time
print(cv2.__version__)

dispW=640
dispH=480
flip=2
font=cv2.FONT_HERSHEY_SIMPLEX
dtav=0

#(If it does not work, try setting to '1' instead of '0')
cam1=cv2.VideoCapture(0)
cam2=cv2.VideoCapture(1)
startTime=time.time()

while True:
    ret, frame1 = cam1.read()
    ret, frame2 = cam2.read()

    frame2=cv2.resize(frame2,(frame1.shape[1],frame1.shape[0]))     #frame2=cv2.resize(frame,(640,480))
    frameCombined=np.hstack((frame1,frame2))

    dt=time.time()-startTime
    startTime=time.time()

    dtav=.9*dtav+.1*dt
    fps=1/dtav

    cv2.imshow('Combo',frameCombined)              #cv2.imshow('Combo',frame2)
    cv2.moveWindow('Combo',0,0)                    #cv2.moveWindow('webCam',0,500) #(high,width)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()