import tkinter as tk
from tkinter import ttk

sc = tk.Tk()
sc.title("More on the window")
# sc.iconbitmap("logo.ico")
sc.geometry('600x400+200+170')
sc.minsize(300, 200)

sc.attributes('-alpha', 0.8)
sc.bind('<Escape>', lambda event:sc.quit())

sc.mainloop()
