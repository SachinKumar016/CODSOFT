from tkinter import *
from random import *

l1=[1,2,3,4,5,6,7,8,9,0]
l2=['a','b','c','d','e','f','g','h','i','j','k',
   'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l3=['!','@','%','^','&','*','_','#']

la=StringVar()
for i in range(5):
    a=randint(0,11)
    la= la + str(a)

w=Tk()
w.title("Password Genrator")
w.geometry("800x500")
result_box = Frame(w, width=250, height=500, bg='white', border=3)
result_box.pack()
b=Label(result_box, textvariable=la)
b.pack()
w.mainloop()