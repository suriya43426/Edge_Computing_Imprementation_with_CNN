#www.bacteria-world.com/cv.jpg  Drag and Drop in my folder 
#copy Code from Lesson1
#learning charging Color , Build Backgroud and Foregroud

import cv2
print(cv2.__version__)

def nothing():
    pass
cv2.namedWindow('Blended')
cv2.createTrackbar('BlendValue','Blended',50,100,nothing)


dispW=320   #colums
dispH=240   #rows
flip=2

cvLogo = cv2.imread('cv.jpg') #อ่านภาพจาก root Folder www.bacteria-world.com/cv.jpg 
cvLogo = cv2.resize(cvLogo,(320,240))
cvLogoGray = cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY) #convert To GrayScale
cv2.imshow('cv Logo Gray', cvLogoGray)
cv2.moveWindow('cv Logo Gray', 0,350)  #แสดงภาพที่ต้องการ Backgroud เป็นสีเทา

_,BGMask = cv2.threshold(cvLogoGray,255,255,cv2.THRESH_BINARY)
cv2.imshow('BG Mask', BGMask)
cv2.moveWindow('BG Mask', 385,100)

FGMask=cv2.bitwise_not(BGMask)
cv2.imshow('FG Mask', FGMask)
cv2.moveWindow('FG Mask',385,350)

FG=cv2.bitwise_and(cvLogo,cvLogo,mask=FGMask)
cv2.imshow('FG', FG)
cv2.moveWindow('FG',703,350)


#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    BG=cv2.bitwise_and(frame,frame,mask=BGMask) #การ and frame จาก Cam เป็น Foregroud
    cv2.imshow('BG',BG)
    cv2.moveWindow('BG',703,100)

    compImage=cv2.add(BG,FG)
    cv2.imshow('compImage',compImage)
    cv2.moveWindow('compImge',1017,100)

    BV=cv2.getTrackbarPos('BlendValue','Blended')/100
    BV2=1-BV

    Blended=cv2.addWeighted(frame,.5,cvLogo,BV2,0)
    cv2.imshow('Blended',Blended)
    cv2.moveWindow('Blended',1017,350)

    FG2=cv2.bitwise_and(Blended,Blended,mask=FGMask)
    cv2.imshow('FG2',FG2)
    cv2.moveWindow('FG2',1324,100)   

    compFinal=cv2.add(BG,FG2)
    cv2.imshow('compFinal',compFinal)
    cv2.moveWindow('comFinal',1324,350)

    cv2.imshow('nanoCam',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

