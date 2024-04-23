import tkinter as tk
from tkinter import ttk

# Window
sc = tk.Tk()
sc.geometry("600x400")
# Title
ttk.Label(master=sc, text="Hi! My name is Akshat Chourey\nConvert Miles to Km", font='calibre 25').pack(pady = 6)

def convert():
    new_value = entry_int.get()*1.61
    output_string.set(str(new_value))


# frame
import_frame = ttk.Frame(master=sc)
entry_int = tk.IntVar()
enter = ttk.Entry(master=import_frame, textvariable=entry_int)
button = ttk.Button(master=import_frame, text="Convert", command=convert)
enter.pack(side='left', padx=6)
button.pack(side='left')
import_frame.pack()

# output, *label can also have its own textVariable
output_string = tk.StringVar()
ttk.Label(master=sc, text="output", font="calibre 24", textvariable=output_string).pack(pady=5)

sc.mainloop()
