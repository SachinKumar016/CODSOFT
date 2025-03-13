import math
class Solution:
    def addition(self,x,y):
        return (x+y)
    
    def subtraction(self,x,y):
        return (x-y)
    
    def multiplication(self,x,y):
        return (x*y)
    
    def divition(self,x,y):
        return (x/y)
    
    def square(self,x,y):
        return (x**y)
    
    def squareroot(self,x,y):
        return (math.sqrt(x,y))
    

def cal():
    option=input("Enter the Option:")
    if(option.lower()=="a"):
        print(result.addition(x,y))
    elif(option.lower()=="b"):
        print(result.subtraction(x,y))
    elif(option.lower()=="c"):
        print(result.multiplication(x,y))
    elif(option.lower()=="d"):
        print(result.divition(x,y))
    elif(option.lower()=="e"):
        print(result.square(x,y))
    elif(option.lower()=="f"):
        print(result.squareroot(x,y))
    else:
        print("Enter the correct option")
        return cal()
c=1
while (c!=0):

    x=int(input("Enter the first no.:"))
    y=int(input("Enter the second no.:"))
    result=Solution()

    print("\n\n\\CALCULATOR\\\n"
    "a. ",x,"add with ",y,
    "\nb. ",x,"subtract by ",y,
    "\nc. ",x,"multiply with ",y,
    "\nd. ",x,"divide by ",y,
    "\ne. ",x,"raise to the power ",y,
    "\nf. sqaure root of ",x,
    "\ng. None of these\n")

    cal()
   
    c=c-1