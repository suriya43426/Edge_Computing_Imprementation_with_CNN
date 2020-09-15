#Python Function
#Classes
#Methods and Threading

#Oject-oriented programming has some advantages over other design patterns.
#Development is fasterr and cheaper, with better software maintainability.
#This in turn, leads to higher-quality software, which is also extensible with new methods and attributes.
#The concept may be too complex for beginners.
#Computationally, OOP software is slower, and use more memory since more lines of code have to be written.


l1=3
w1=5
area1=l1*w1
print('area of rectangle 1: ,' ,area1)

l2=6
w2=4
area2=l2*w2
print('area of rectangle 2: ,' ,area2)

#------------------------------------
#------------------------------------

def RectCalc(w,l):
    area=w*l
    per=2*w+2*l
    return area,per

l1=3
w1=5
area1,per1=RectCalc(w1,l1)
print('area of rectangle 1: ,' ,area1,per1)

l2=6
w2=4
area2,per2=RectCalc(w2,l2)
print('area of rectangle 2: ,' ,area2,per2)


