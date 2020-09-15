#bacteria-world.com/pl.jpg
#copy code Lesson1

import cv2
print(cv2.__version__)

dispW=640
dispH=480
flip=2

#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
 
PL=cv2.imread('pl.jpg')
PL=cv2.resize(PL,(75,75))   #ลดขนาด Logo

cv2.imshow('LogoWindow',PL)
cv2.moveWindow('LogoWindow',700,0)   #x 700,y 0

PLGray=cv2.cvtColor(PL,cv2.COLOR_BGR2GRAY) #ได้ภาพสีเทา
cv2.imshow('PLGray',PLGray)
cv2.moveWindow('PLGray',800,0) #x 800,y 0

_,BGMask=cv2.threshold(PLGray,245,255,cv2.THRESH_BINARY) #ได้ภาพสีขาวดำชัดเจน 100-> 245 ขาวมาก
cv2.imshow('BGMask',BGMask)
cv2.moveWindow('BGMask',900,0) #x 900,y 0

FGMask=cv2.bitwise_not(BGMask)  #ตรงข้ามกับ BGMask
cv2.imshow('FGMask',FGMask)
cv2.moveWindow('FGMask',900,0) #x 1000,y 0

FG=cv2.bitwise_and(PL,PL,mask=FGMask) # *** ตัดขอบ ขาวออกแล้ว รวมภาพสี
cv2.imshow('FG',FG)
cv2.moveWindow('FG',1100,0)

#Box moving around
BW=75
BH=75       #W,H
Xpos=10
Ypos=10     #position
dX=1
dY=1

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
                                            
    ROI=frame[Ypos:Ypos+BH, Xpos:Xpos+BW]   #ROI : Region of Interest
    
    ROIBG=cv2.bitwise_and(ROI,ROI,mask=BGMask)
    cv2.imshow('ROIBG',ROIBG)
    cv2.moveWindow('ROIBG',1200,0)      #-> First ROI Backgroud Logo 75x75

    ROInew=cv2.add(FG,ROIBG)
    cv2.imshow('ROInew',ROInew)
    cv2.moveWindow('ROInew',1300,0)
    frame[Ypos:Ypos+BH,Xpos:Xpos+BW]=ROInew  #=> Full screen add Logo 

    Xpos=Xpos+dX                    #frame [Y10+75,X10+75]-> การขยับที่ละ Step
    Ypos=Ypos+dY                    #1
                    
    if Xpos<=0 or Xpos+BW>=dispW:   #2
        dX=dX*(-1)              

    if Ypos<=0 or Ypos+BH>=dispH:   #3
        dY=dY*(-1)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)       #you see camera normal work

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()