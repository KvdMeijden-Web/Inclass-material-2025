import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treasure Chest")
root.geometry("400x300")
root.config(bg="sandybrown")

#make a varibel to store the text entry
text_entry = tk.Entry(root, width=30)
text_entry.grid(row=0, column=0, padx=10, pady=10)
text_entry.insert(0, "........")
# place the text entry on the interface


root.mainloop()