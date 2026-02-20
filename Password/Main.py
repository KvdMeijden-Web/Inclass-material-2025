from tkinter import *
from tkinter import ttk
import json

class Interface:
    def __init__(self, screen):
        self.screen = screen
        self.screen.title("Password Manager")
        self.screen.geometry("620x400")
        self.screen.config(bg="lightblue")
        self.title = Label(self.screen, text="Welcome to Password Manager", bg="lightblue", font=("Arial", 16))
        self.title.grid(row=0, column=0, columnspan=2, pady=10)
        
      
class passwords:
    def __init__(self):
        self.passwordlist = ttk.Treeview (screen, columns=("Username", "Description"), show='headings')
        self.passwordlist.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.passwordlist.heading("Username", text="Username")
        self.passwordlist.heading("Description", text="Description")
        
        with open("Password/Passwords.json", "r") as file:
            self.data = json.load(file)
        for username in self.data:
            password = self.data[username][0]
            description = self.data[username][1]
            self.passwordlist.insert("", "end", values=(username, description))
        self.passwordshow = Label(screen, text="password", bg="white", font=("Arial", 12))
        self.passwordshow.grid(row=2, column=0, columnspan=2, pady=10)
        
    def show_password(self, event):
            selected_item = self.passwordlist.selection()[0]
            password = self.data[self.passwordlist.item(selected_item)["values"][0]][0]
            self.passwordshow.config(text=f"Password: {password}")



if __name__ == "__main__":
    screen = Tk()
    Interface(screen)
    passwords()
    show_password = passwords.show_passwordp.passwordlist.selection())

    screen.mainloop()
