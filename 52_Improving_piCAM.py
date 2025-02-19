# Gstreamer code for improvded Raspberry Pi Camera Quality
camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.2 saturation=1.2 ! appsink'

import cv2
print(cv2.__version__)
dispW=1280
dispH=720
flip=2
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.2 saturation=1.2 !  appsink'
cam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#cam=cv2.VideoCapture('/dev/video1')
while True:
    ret, frame = cam.read()
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

#Option 1: Launch the cameras using OpenCV
import jetson.inference
import jetson.utils
import cv2
import numpy as np
import time
width=1280
height=720
dispW=width
dispH=height
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance  contrast=1.5 brightness=-.3 saturation=1.2 ! appsink  '
cam1=cv2.VideoCapture(camSet)
#cam1=cv2.VideoCapture('/dev/video1')
#cam1.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
#cam1.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
net=jetson.inference.imageNet('alexnet')
font=cv2.FONT_HERSHEY_SIMPLEX
timeMark=time.time()
fpsFilter=0
while True:
    _,frame=cam1.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    img=jetson.utils.cudaFromNumpy(img)
    classID, confidence =net.Classify(img, width, height)
    item=''
    item =net.GetClassDesc(classID)
    dt=time.time()-timeMark
    fps=1/dt
    fpsFilter=.95*fpsFilter +.05*fps
    timeMark=time.time()
    cv2.putText(frame,str(round(fpsFilter,1))+' fps '+item,(0,30),font,1,(0,0,255),2)
    cv2.imshow('recCam',frame)
    cv2.moveWindow('recCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.releast()
cv2.destroyAllWindows()

#Option 2: Control Camera with NVIDIA Jetson Utiltties Library
import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np
width=1280
height=720
#cam=jetson.utils.gstCamera(width,height,'/dev/video1')
cam=jetson.utils.gstCamera(width,height,'0')
net=jetson.inference.imageNet('googlenet')
timeMark=time.time()
fpsFilter=0
timeMark=time.time()
font=cv2.FONT_HERSHEY_SIMPLEX
while True:
    frame, width, height = cam.CaptureRGBA(zeroCopy=1)
    classID, confidence = net.Classify(frame, width, height)
    item = net.GetClassDesc(classID)
    dt=time.time()-timeMark
    fps=1/dt
    fpsFilter=.95*fpsFilter+.05*fps
    timeMark=time.time()
    frame=jetson.utils.cudaToNumpy(frame,width,height,4)
    frame=cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR).astype(np.uint8)
    cv2.putText(frame,str(round(fpsFilter,1))+'      '+item,(0,30),font,1,(0,0,255),2)
    cv2.imshow('webCam',frame)
    cv2.moveWindow('webCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()