#What is tkinter?
#GUI library for python
#event driven programming:
    # the program is a continuous loop.
    # the program waits for user input/events.
    # when an event occurs, the program responds to it.
    # the speed of each loop is linked to the frame rate in games.

#initialising tkinter
# We import both tkinter and ttk (themed tkinter) modules. 


# first create a screen object a screen is called a canvas or window as well
# a screen has a resolution (width x height) these are in pixels.
# you can find all the options for a tkinter window online.

import tkinter as tk
from tkinter import ttk, messagebox


screen = tk.Tk()
screen.title("Calculator")
screen.geometry("450x250")

style = ttk.Style()
style.theme_use("vista")

def calculate():
    # get value number 1
    num1 = float(first_entry.get())
    # get value number 2
    num2 = float(second_entry.get())
    # get the symbol
    symb = symbol.get()
    #caculate the result
    if symb == "+":
        result = num1 + num2
    elif symb == "-":
        result = num1 - num2
    elif symb == "*":
        result = num1 * num2
    elif symb == "/":
        if num2== 0:
           messagebox.showerror("Error", "Cannot divide by 0!")
           return
        else:
            result = num1 / num2
    elif symb == "%":
        result = num1 % num2
    result_label.config(text=f"Result: {result}")
    first_entry.delete(0, tk.END)
    first_entry.insert(0, result)
    second_entry.delete(0, tk.END)

def reset():
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    symbol.set("")
    result_label.config(text="Result:")

title = ttk.Label(screen, text="Koen's amazing calculator", font=("Arial", 16))
# test_label.pack(padx=10, pady=50)
title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

first_entry = ttk.Entry(screen, width=10)
first_entry.grid(row=1, column=0, padx=5, pady=5, stick="e")

symbol = ttk.Spinbox(screen, values=("+", "-", "*", "/","%"), width=3, justify="center")
symbol.grid(row=1, column=1, padx=5, pady=10)

second_entry = ttk.Entry(screen, width=10)
second_entry.grid(row=1, column=2, padx=5, pady=5, stick="w")

Calculate_button = ttk.Button(screen, text="Calculate", width=25, command=calculate)
Calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

Reset_button = ttk.Button(screen, text="Reset", width=10, command=reset)
Reset_button.grid(row=2, column=2, padx=10, pady=10)

result_label = ttk.Label(screen, text="Result: ", font=("Arial", 16))
result_label.grid(row=3, column=1, padx=10, pady=10)


# test_label_too = ttk.Label(screen, text="this is also a test label", font=("Arial", 16))
# test_label_too.pack(padx=10, pady=50)

# test_button = ttk.Button(screen, text="this is a test button")
# test_button.pack(padx=10, pady=10)

screen.mainloop()