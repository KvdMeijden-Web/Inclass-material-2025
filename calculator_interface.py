from tkinter import *
from tkinter import ttk


def calculate():
    num1 = float(first.get())
    num2 = float(second.get())
    op = operation.get()
    if op == '+':
        result = num1 + num2
        first.delete(0, END)
        first.insert(0,result)
    elif op == '-':
        result = num1 - num2
        first.delete(0, END)
        first.insert(0,result)
    elif op == '*':
        result = num1 * num2
        first.delete(0, END)
        first.insert(0,result)
    elif op == '/':
        if num2 == 0:
            result = "can't divede by zero"
        else:
            result = num1 / num2
            first.delete(0, END)
            first.insert(0,result)
    elif op == '%':
        result = num1 % num2
        first.delete(0, END)
        first.insert(0,result)
    else:
        result = "Invalid operation"
    
    result_label.config(text=f"Result: {result}")
    
    second.delete(0, END)

def reset():
    first.delete(0, END)
    second.delete(0, END)
    operation.set('')
    result_label.config(text="Result: ")

screen = Tk()

screen.title("Interface Example")

Welcome = ttk.Label(screen, text="Welcome to the calculator", font=("Arial", 16))
Welcome.grid(column=1,row=0, padx=10, pady=10)

Instruction = ttk.Label(screen, text="enter the numbers, and operation", font=("Arial", 16))
Instruction.grid(column=1,row=1, padx=10, pady=10)

first = ttk.Entry(screen, width=20, justify=CENTER)
first.grid(column=1,row=2, padx=10, pady=10)

operation_var = StringVar(value='+')
operation = ttk.Spinbox(screen, textvariable=operation_var, values=('+', '-', '*', '/','%'), width=2, justify=CENTER)
operation.grid(column=1,row=3, padx=10, pady=10)

second = ttk.Entry(screen, width=20, justify=CENTER)
second.grid(column=1,row=4, padx=10, pady=10)

button = ttk.Button(screen, text="calculate",command=calculate)
button.grid(column=0, row=2, padx=10, pady=10)

button = ttk.Button(screen, text="reset",command=reset)
button.grid(column=2, row=2, padx=10, pady=10)

result_label = ttk.Label(screen, text="Result: ", font=("Arial", 14))
result_label.grid(column=1, row=5, padx=10, pady=10)
screen.mainloop()
