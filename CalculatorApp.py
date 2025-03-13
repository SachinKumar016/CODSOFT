from tkinter import *

m=Tk(screenName="Calculator",baseName=None, className="Calculator")
m.geometry("500x200")

input_box=Frame(m, bd=5,relief="groove",padx=1,pady=1, width=250,height=150, bg='white', border=3)
input_box.pack(anchor="nw")
input_box.grid_propagate(False)
Label(input_box, text='First Name', bg='white').grid(row=0, padx=5, pady=5)
Label(input_box, text='Last Name' , bg='white').grid(row=1, padx=5, pady=5)
x = Entry(input_box)
y = Entry(input_box)
x.grid(row=0, column=1, padx=5, pady=5)
y.grid(row=1, column=1, padx=5, pady=5)

m.mainloop()