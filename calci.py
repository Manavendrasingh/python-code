import operator
import math
 #BLL
class calci:
    def __init__(self):#costrecter or intences
        self.x=0
        self.y=0
        self.z=0
    def add(self):
        self.z = operator.add(self.x,self.y)
    def sub(self):
        self.z = (self.x-self.y)
    def multi(self):
        self.z = self.x*self.y
    def div(self):
        self.z = self.x/self.y
    def pow(self):
        self.z = math.pow(self.x,self.y)
    def log(self):
        self.z=l


while(1):
     ob=calci()
     #ob.x=int(input("enter the fist no"))
     #ob.y=int(input("enter the second no"))
     print("enter +,*,/,-,pow,0 for exit")
     ch=input("enter the choice")
     if ch=='+':
         ob.x = int(input("enter the fist no"))
         ob.y = int(input("enter the second no"))
         ob.add()
         print(ob.z)
     elif ch=='-':

         ob.x = int(input("enter the fist no"))
         ob.y = int(input("enter the second no"))
         ob.sub()
         print(ob.z)
     elif ch=='*':

         ob.x = int(input("enter the fist no"))
         ob.y = int(input("enter the second no"))
         ob.multi()
         print(ob.z)
     elif ch=='/':

         ob.x = int(input("enter the fist no"))
         ob.y = int(input("enter the second no"))
         ob.div()
         print(ob.z)
     elif ch=='pow':

         ob.x = int(input("enter the fist no"))
         ob.y = int(input("enter the second no"))
         ob.pow()
         print(ob.z)
     elif ch=='0':
         exit()


