#import from Lesson1
#home work this week = 0->255 Hue,Staturation RGB, 

import cv2
import numpy as np
print(cv2.__version__)

dispW=640
dispH=480
flip=2

#Uncomment These next Two Line for Pi Camera
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam=cv2.VideoCapture(0)

blank=np.zeros([480,640,1],np.uint8)    #unsicneINT_8_bits
#blank[0:240,0:320]=125                  # 0 -> 125 ,255=white,125=gray
                                        #สร้าง BoxGray ขนาด 240 h(rows), 320 w(colums)
while True:
    ret, frame = cam.read()             #add  martix 
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    print(frame.shape)                 #sum number of rows , sum number of colums
    print(frame.size)

    b=cv2.split(frame)[0]               #แบ่งช่องสี [b,g,r] -> [0,1,2]
    g=cv2.split(frame)[1]
    r=cv2.split(frame)[2]
    
    #b=b*1.2                             #veryboots blue
    r[:]=b[:]*.5                         # pass parameter red and blue channel x 0.5
    b,g,r=cv2.split(frame)  

    blue=cv2.merge((b,blank,blank))
    green=cv2.merge((blank,g,blank))
    red=cv2.merge((blank,blank,r))

    merge=cv2.merge(b,g,r)              #--> test b,g,r  , g,r,b

    cv2.imshow('blue',blue)
    cv2.moveWindow('blue',700,0)

    cv2.imshow('green',green)
    cv2.moveWindow('green',0,500)
    
    cv2.imshow('red',red)
    cv2.moveWindow('red',700,500)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    #cv2.imshow('blank',blank)
    #cv2.moveWindow('blank')

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()



#print  
#(480,640,3)
#(480,640,3)
#(480,640,3)
#(480,640,3)
#(480,640,3)
#(480,640,3)
#(480,640,3)

#gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#(480,640)
#(480,640)
#(480,640)
#(480,640)

#print(frame.shape) 
#print(frame.shape) 

#(480,640,3)
#921600