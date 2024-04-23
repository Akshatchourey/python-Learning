import tkinter as tk
from tkinter import ttk

sc = tk.Tk()
sc.geometry('600x400')

# Buttons
def button_fun():
    print("I am a simple Button")


button = ttk.Button(sc, text="press me", command=button_fun)
button.pack()
# Check Button
check_var = tk.BooleanVar()
check_Button = ttk.Checkbutton(
    sc, text="checked or not",
    variable=check_var,
    command=lambda: print(check_var.get()))
check_Button.pack()

# Radio Button
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    sc, text="RadioButton1",
    value="radio1",
    variable=radio_var,
    command=lambda: print(radio_var.get()))
radio2 = ttk.Radiobutton(sc, text="RadioButton2", value=5, variable=radio_var, command=lambda: print(radio_var.get()))
radio1.pack()
radio2.pack()

sc.mainloop()
