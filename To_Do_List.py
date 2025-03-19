from tkinter import *
w=Tk()
w.title("omala")
w.geometry("500x500")
input_box = Frame(w, bd=5, relief="ridge", width=500, height=100, bg='white', border=3)
a=Label(input_box, text="saachin")
input_box.pack()
a.pack()
w.mainloop()