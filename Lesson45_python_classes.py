#Python Function
#Classes
#Methods and Threading

class Rectangle:
    def __init__(self,c,w,l):
        self.color=c
        self.width=w
        self.length=l
        #self.area=self.width*self.length
    def area(self):
        self.area=self.width*self.length
        return self.area
    def per(self):
        self.perimeter=2*self.width+2*self.length
        #กว้างx2 + ยาวx2
        return self.perimeter
        
c1='red'
w1=3
l1=4
rect1=Rectangle(c1,w1,l1)
areaRect1=rect1.area()
print(areaRect1)

c2='blue'
w2=6
l2=7
rect2=Rectangle(c2,w2,l2)
areaRect2=rect2.area()
print(areaRect2)

per1=rect1.per()

print('Rectangle 1 has perimeter: ', rect1.color)
#----------------------------------
#----------------------------------
#perimeter เส้นรอบรูป 

