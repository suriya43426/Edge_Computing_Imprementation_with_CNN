#import from Lesson1

import cv2
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

while True:
    ret, frame = cam.read()             #add  martix 
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    print(frame.shape)                 #sum number of rows , sum number of colums
    print(frame.size)

    b=cv2.split(frame)[0]               #แบ่งช่องสี [b,g,r] -> [0,1,2]
    g=cv2.split(frame)[1]
    r=cv2.split(frame)[2]

    cv2.imshow('blue',b)
    cv2.moveWindow('blue',700,0)

    cv2.imshow('green',g)
    cv2.moveWindow('green',0,500)
    
    cv2.imshow('red',r)
    cv2.moveWindow('red',700,500)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

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