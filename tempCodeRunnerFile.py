from tkinter import *
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
    

m=Tk(screenName="Calculator",baseName=None, className="Calculator")
m.geometry("500x200")


input_box=Frame(m, bd=5,relief="groove", width=246,height=150, bg='white', border=3)
input_box.grid(row=0, column=0, sticky="ne", padx=1, pady=1)
input_box.grid_propagate(False)

Label(input_box, text='First Name', bg='white').grid(row=0, padx=5, pady=5)
Label(input_box, text='Last Name' , bg='white').grid(row=1, padx=5, pady=5)
x = Entry(input_box)
y = Entry(input_box)
x.grid(row=0, column=1, padx=5, pady=5)
y.grid(row=1, column=1, padx=5, pady=5)

result_box=Frame(m,bd=5,relief="groove", width=246,height=150, bg='white', border=3)
result_box.grid(row=0, column=1, sticky="ne", padx=1, pady=1)
input_box.grid_propagate(False)



m.mainloop()