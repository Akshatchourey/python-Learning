import tkinter as tk
from tkinter import ttk

sc = tk.Tk()
sc.geometry('600x400')

items = ["pizza","ice cream","broccoli"]
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(sc, textvariable=food_string)
combo['values'] = items
combo.pack()
combo.bind('<<ComboboxSelected>>', lambda event: print(food_string.get()))

spin = ttk.Spinbox(sc, from_=1, to=20, increment=3)
spin.pack()
spin.bind('<<Increment>>', lambda event:print("up"))
spin.bind('<<Decrement>>', lambda event:print("down"))

sc.mainloop()
