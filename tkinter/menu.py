import tkinter as tk
from tkinter import ttk

sc = tk.Tk()
sc.geometry("600x400")

# menu
menu = tk.Menu()
# Sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="New", command= lambda: print("New file"))
file_menu.add_command(label="Open", command= lambda: print("Opening file"))
resent_files = tk.Menu(file_menu, tearoff=False)
resent_files.add_command(label="file1", command=lambda: print("file first"))
resent_files.add_command(label="file2", command=lambda: print("file second"))
resent_files.add_command(label="file3", command=lambda: print("file third"))
file_menu.add_cascade(label="Resent Files", menu=resent_files)
file_menu.add_separator()
file_menu.add_command(label="Save", command= lambda: print("Saving"))
file_menu.add_command(label="Save As..", command= lambda: print("Saving As..."))

help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label="help", command=lambda: print("Helping one sec..."))
help_menu.add_checkbutton(label="Check")

menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Help", menu=help_menu)
sc.config(menu = menu)

sc.mainloop()
