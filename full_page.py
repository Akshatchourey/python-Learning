from tkinter import *
aks = Tk()
aks.geometry("500x600")
button = Button(text="good morning", bg='gray', fg='red')
button.pack(side=TOP, anchor="ne")
canvas = Canvas(height=850, width=850)
canvas.pack(side=BOTTOM, anchor="se")
frame = Frame(aks, bg='blue')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

aks.mainloop()
