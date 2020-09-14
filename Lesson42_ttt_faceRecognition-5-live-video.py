import face_recognition
import cv2
import os
import pickle

print(cv2.__version__)

Encodings=[]
Names=[]

with open('train.pkl','rb') as f:
    Names=pickle.load(f)
    Encodings=pickle.load(f)
font=cv2.FONT_HERSHEY_SIMPLEX
cam=cv2.VideoCapture(1)

while True:
    _,frame=cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    facePositions=face_recognition.face_locations(frameRGB,model='cnn')     #testRunning
    allEncodings=face_recognition.face_encodings(frameRGB,facePositions)    #Encodeing 

    for (top,right,bottom,left), face_encoding in zip(facePositions,allEncodings):
        name:'Unknow Person'
        matches=face_recognition.compare_faces(Encodings,face_encoding)

        if True in matches:
            first_match_index=matches.index(True)
            name=Names[first_match_index]
        top=top*3
        right=right*3
        bottom=bottom*3
        left=left*3
        cv2.rectangle(frame,(left,top),(right,bottom),font,(0,0,255),2)
        cv2.putText(frame,name,(left,top-6),font,.75(0,0,255),2)
    
    cv2.imshoww('Picture',frame)
    cv2.moveWindow('Picture',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyALLWindows()