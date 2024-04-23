import tkinter as tk
from tkinter import ttk

sc = tk.Tk()
sc.geometry('400x600')

label1 = ttk.Label(sc, text="label 1", background="red")
label2 = ttk.Label(sc, text="label 2", background="blue")
label3 = ttk.Label(sc, text="label 3", background="green")
button = ttk.Button(sc, text="Button")

# label1.pack(side="left", expand=True, fill='both')
# label2.pack(side="left", expand=True, fill='y')

# grid
# sc.columnconfigure(0, weight=1)
# sc.columnconfigure(1, weight=1)
# sc.columnconfigure(2, weight=2)
# sc.rowconfigure(0, weight=1)
# sc.rowconfigure(1, weight=1)
# label1.grid(row=0, column=1, sticky='nsew')
# label2.grid(row=1, column=1, columnspan=2, sticky='nsew')

# exercise
label1.pack(side='top',expand=True, fill='both', padx=10, pady=10)
label2.pack(side='left',expand=True, fill='both')
label3.pack(side='top',expand=True, fill='both')
button.pack(side='top',expand=True, fill='both')

sc.mainloop()
