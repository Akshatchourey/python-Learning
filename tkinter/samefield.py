import tkinter as tk
from tkinter import ttk

sc = tk.Tk()
sc.geometry('600x450')
sc.title('Getting and setting widgets')

string_var = tk.StringVar()
label = ttk.Label(master=sc, text="Some Text", textvariable=string_var)
label.pack(pady=6)
# print(label.configure())
entry = ttk.Entry(master=sc, textvariable=string_var)
entry.pack(side='left', pady=6)

button = ttk.Button(master=sc, text="press")
button.pack(side='left')

sc.mainloop()

