from tkinter import *
from PIL import Image, ImageTk
from random import choice

def hide_image():
    image_label.config(image="", fg="gray")

def play_game():
    global hide_timer

    user_selection = user_choice.get()
    
    if not user_selection:
        result_label.config(text="Please select Rock, Paper, or Scissors!", fg="red")
        return

    computer_selection = choice(list(image_files.keys()))
    image_label.config(image=image_list[computer_selection], text="")

    if hide_timer:
        w.after_cancel(hide_timer)

    hide_timer = w.after(6000, hide_image)

    if user_selection == computer_selection:
        result = "DRAW"
        color = "blue"
    elif (user_selection == "Rock" and computer_selection == "Scissors") or \
         (user_selection == "Scissors" and computer_selection == "Paper") or \
         (user_selection == "Paper" and computer_selection == "Rock"):
        result = "YOU WIN"
        color = "green"
    else:
        result = "YOU LOSE"
        color = "red"

    result_label.config(text=result, fg=color)

w = Tk()
w.title("Rock Paper Scissors")
w.geometry("600x500")
image_files = {"Rock": "Rock.jpg", "Paper": "Paper.jpg", "Scissors": "Scissor.png"}
image_list = {key: ImageTk.PhotoImage(Image.open(img).resize((200, 200))) for key, img in image_files.items()}
user_choice = StringVar()
hide_timer = None
image_frame = Frame(w, width=200, height=200, relief="solid", bd=2)
image_frame.pack(pady=20)
image_frame.pack_propagate(False)
image_label = Label(image_frame, width=200, height=200, fg="gray")
image_label.pack()


button = Button(w, text="Check", command=play_game, font=("Arial", 12))
button.pack(pady=10)
result_label = Label(w, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)
user_frame = Frame(w)
user_frame.pack(side=BOTTOM, pady=60)

Label(user_frame, text="Choose:", font=("Arial", 12)).pack()
for option in ["Rock", "Paper", "Scissors"]:
    Radiobutton(user_frame, text=option, variable=user_choice, value=option, font=("Arial", 12)).pack(side=LEFT)

w.mainloop()
