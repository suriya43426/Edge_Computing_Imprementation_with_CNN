import cv2
import numpy as np

print(cv2.__version__)
#copy from Lesson1

dispW=640
dispH=480
flip=2 

img1=np.zeros((480,640,1) ,np.uint8) #row 480,colums 640,grayScale 1 color
img1[0:480, 0:320]=[255] #Below Screen White and Black

img2=np.zeros((480,640,1),np.uint8)
img2[190:290,270:370]=[255]

bitAnd =cv2.bitwise_and(img1,img2)

bitOr =cv2.bitwise_or(img1,img2)

bitXor =cv2.bitwise_xor(img1,img2)

#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    cv2.imshow('nanoCam',frame)     #raspberryPiCam is runing
    cv2.moveWindow('nanoCam',0,0)   #ขยับจอ ซ้ายบน
   
    cv2.imshow('img1',img1)         #โชว์ หน้าจอใหม่ชื่อ img1
    cv2.moveWindow('img1',0,500)    #ขยับจอ ซ้ายล่าง
   
    cv2.imshow('img2',img2)         #โชว์ หน้าจอใหม่ชื่อ img2
    cv2.moveWindow('img2',700,0)    #ขยับจอขวาบน        

    cv2.imshow('AND',bitAnd)        #โชว์ หน้าจอใหม่ชื่อ AND
    cv2.moveWindow('AND',700,500)   #ขยับจอ ขวาล่างแสดงการ And ของ img1, img2

    cv2.imshow('OR',bitOr)          #โชว์ หน้าจอใหม่ชื่อ OR
    cv2.moveWindow('OR',1350,0)     #ขยับจอ ขวาบนแสดงการ Or ของ img1, img2

    cv2.imshow('XOR',bitXor)        #โชว์ หน้าจอใหม่ชื่อ XOR
    cv2.moveWindow('XOR',1350,500)  #ขยับจอ ขวาล่างแสดงการ Xor ของ img1, img2

    frame=cv2.bitwise_and(frame,frame,mask=img1) #แสดงครึ่งจอ ขวาดำ
    #frame=cv2.bitwise_and(frame,frame,mask=img2) #แสดง ภาพสี่เหลี่ยมเล็ก นอกนนั้นดำ
    #frame=cv2.bitwise_and(frame,frame,mask=bitXor) #แสดง หน้าจอเฉพาะ Xor
    cv2.imshow('nanoCam',frame)    
    cv2.moveWindow('nanoCam',0,0) 

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

#showTerminal [[255 255 255] 
#showTerminal  [255 255 255] ...
#showTerminal  [255 255 255]]