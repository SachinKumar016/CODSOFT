import random
import string
from tkinter import *

def generate_password():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # a-z, A-Z
    if use_numbers:
        characters += string.digits  # 0-9
    if use_symbols:
        characters += string.punctuation

    if characters:
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    else:
        password_var.set("Select at least one option!")


root = Tk()
root.title("Password Generator")
root.geometry("400x300")
Label(root, text="Password Generator", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)
Label(root, text="Password Length:", bg="#f0f0f0").pack()
length_entry = Entry(root)
length_entry.pack(pady=5)

letters_var = BooleanVar(value=True)
numbers_var = BooleanVar(value=True)
symbols_var = BooleanVar(value=True)

Checkbutton(root, text="Include Letters", variable=letters_var, bg="#f0f0f0").pack()
Checkbutton(root, text="Include Numbers", variable=numbers_var, bg="#f0f0f0").pack()
Checkbutton(root, text="Include Symbols", variable=symbols_var, bg="#f0f0f0").pack()

bu=Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white")
bu.pack(pady=10)

password_var = StringVar()
Entry(root, textvariable=password_var, width=30, font=("Arial", 12), bd=2, relief="solid").pack(pady=10)

root.mainloop()
