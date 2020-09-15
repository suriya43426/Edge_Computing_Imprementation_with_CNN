#Python Function
#Classes
#Methods and Threading

# using library threading 

from threading import Thread
import time

def BigBox(color,l):
    while True:
        print(color,'Big Box is Open')
        time.sleep(5)
        print(color,'Big Box is Closed')
        time.sleep(5)

def SmallBox(color,l):
    while True:
        print(color,'Small Box is Open')
        time.sleep(1)
        print(color,'Small Box is Closed')
        time.sleep(1)
c='red'
x=5
bigBoxThread=Thread(target=BigBox, args=(c,x))
c='blue'
x=4
smallBoxThread=Thread(target=SmallBox, args=(c,x))

bigBoxThread.daemon=True
smallBoxThread.daemon=True

bigBoxThread.start()
smallBoxThread.start()

while True:
    pass
