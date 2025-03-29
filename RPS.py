from tkinter import *
from PIL import Image, ImageTk
from random import randint
def computer_choose():
    a = randint(1, 31)
    if a in (1, 3, 6, 18, 24, 11, 27, 15, 22, 19):
        n = 0
    elif a in (2, 4, 7, 17, 12, 21, 25, 30, 9, 14):
        n = 1
    else:
        n = 2
    label.config(image=image_list[n])
w = Tk()
w.title("Rock Paper Scissors")
w.geometry("600x500")
image_files = ["Rock.jpg", "Paper.jpg", "Scissor.png"]
image_list = [ImageTk.PhotoImage(Image.open(img).resize((200, 200))) for img in image_files]

label = Label(w, image=image_list[0]) 
label.pack(pady=10)
button = Button(w, text="Check", command=computer_choose, font=("Arial", 12))
button.pack()

option=Frame(w, width="50", height="300")

w.mainloop()
