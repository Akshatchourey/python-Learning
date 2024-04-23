import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("College Transactions")
        self.geometry("920x610+175+90")
        style = ttk.Style()
        print(style.theme_names())
        style.theme_use('classic')
        ttk.Label(text="Text Here").pack()
        ttk.Button(text="Click Me..").pack(side='left')


if __name__ == "__main__":
    app = App()
    app.mainloop()
