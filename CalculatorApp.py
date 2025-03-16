from tkinter import *
import math

# Function to perform operations
def addition():
    try:
        x = float(x1.get())
        y = float(y1.get())
        eq.set(str(x + y))
    except ValueError:
        eq.set("Error")

def subtraction():
    try:
        x = float(x1.get())
        y = float(y1.get())
        eq.set(str(x - y))
    except ValueError:
        eq.set("Error")

def multiplication():
    try:
        x = float(x1.get())
        y = float(y1.get())
        eq.set(str(x * y))
    except ValueError:
        eq.set("Error")

def division():
    try:
        x = float(x1.get())
        y = float(y1.get())
        if y == 0:
            eq.set("Cannot divide by zero")
        else:
            eq.set(str(x / y))
    except ValueError:
        eq.set("Error")

def square():
    try:
        x = float(x1.get())
        eq.set(str(x ** 2))
    except ValueError:
        eq.set("Error")

def squareroot():
    try:
        x = float(x1.get())
        if x < 0:
            eq.set("Invalid Input")
        else:
            eq.set(str(math.sqrt(x)))
    except ValueError:
        eq.set("Error")

# Create the main Tkinter window
m = Tk()
m.title("Calculator")
m.geometry("500x300")

# Input Frame
input_box = Frame(m, bd=5, relief="groove", width=250, height=100, bg='white', border=3)
input_box.grid(row=0, column=0, sticky="n", padx=10, pady=10)

Label(input_box, text='First Number:', bg='white').grid(row=0, column=0, padx=5, pady=5)
Label(input_box, text='Second Number:', bg='white').grid(row=1, column=0, padx=5, pady=5)

x1 = Entry(input_box)
y1 = Entry(input_box)
x1.grid(row=0, column=1, padx=5, pady=5)
y1.grid(row=1, column=1, padx=5, pady=5)

# Result Box
result_box = Frame(m, bd=5, relief="groove", width=250, height=50, bg='white', border=3)
result_box.grid(row=0, column=1, sticky="n", padx=10, pady=10)

eq = StringVar()
result = Entry(result_box, textvariable=eq, font=("Arial", 14), width=20, state="readonly")
result.pack()

# Buttons
button_frame = Frame(m)
button_frame.grid(row=1, column=0, columnspan=2, pady=10)

Button(button_frame, text="+", command=addition, width=10).grid(row=0, column=0, padx=5, pady=5)
Button(button_frame, text="-", command=subtraction, width=10).grid(row=0, column=1, padx=5, pady=5)
Button(button_frame, text="*", command=multiplication, width=10).grid(row=1, column=0, padx=5, pady=5)
Button(button_frame, text="/", command=division, width=10).grid(row=1, column=1, padx=5, pady=5)
Button(button_frame, text="x²", command=square, width=10).grid(row=2, column=0, padx=5, pady=5)
Button(button_frame, text="√x", command=squareroot, width=10).grid(row=2, column=1, padx=5, pady=5)

# Run the Tkinter main loop
m.mainloop()
