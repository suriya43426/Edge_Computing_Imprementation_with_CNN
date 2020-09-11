# in command line root repo

# sudo apt-get update

# sudo apt-get install cmake libopenblas-dev liblapack-dev libjpeg-dev

# git clone https://github.com/JetsonHacksNano/installSwapfile

# ./installSwapfile/installSwapfile.sh

# sudo reboot 






# wget http://dlib.net/files/dlib-19.17.tar.bz2

# tar jxvf dlib-19.17.tar.bz2

# cd /dlib-19.17/dlib/cuda     gedit cudnn_dlibapi.cpp  

# run editor and   search // forward algo  fix

# cd..    ~/dlib-19.17/   ls  from root

# sudo python3 setup.py install 

# ~/dlib-19.17/  sudo  pip3 install face_recognition

#if successfully installed face-recognition-1.3.0

import face_recognition

image = face_recognition.load_image_file('/home/pjm/Desktop/pyPro')

face_locations=face_recognition.face_locations(image)

print(face_locations)
