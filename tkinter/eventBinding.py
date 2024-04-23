import tkinter as tk
from tkinter import ttk

sc = tk.Tk()
sc.geometry('800x600')
sc.title("Learning Event")

# widgets
text = tk.Text(sc)
entry = ttk.Entry(sc)
button = ttk.Button(sc, text="press me")

# layout
text.pack()
entry.pack()
button.pack()

# event
sc.bind('<Alt-KeyPress-a>', lambda event: print("this is an event"))
text.bind('<KeyPress>', lambda event: print(f"The pressed {event.char} "))

sc.mainloop()
