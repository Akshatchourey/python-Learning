from tkinter import *
al = Tk()
al.geometry("495x350")
al.minsize(495, 350)
al.title("chourey's calculator")

but1 = Button(text="1", bg="white", fg="black", font="comic 11 bold", height=4, width=6, borderwidth=4).grid(row=1, column=1)
but2 = Button(text="2", bg="white", fg="black", font="comic 11 bold", height=4, width=6, borderwidth=4).grid(row=1, column=2)
but3 = Button(text="3", bg="white", fg="black", font="comic 11 bold", height=4, width=6, borderwidth=4).grid(row=1, column=3)
but4 = Button(text="4", bg="white", fg="black", font="comic 11 bold", height=4, width=6, borderwidth=4).grid(row=2, column=1)
but5 = Button(text="5", bg="white", fg="black", font="comic 11 bold", height=4, width=6, borderwidth=4).grid(row=2, column=2)
but6 = Button(text="6", bg="white", fg="black", font="comic 11 bold", height=4, width=6, borderwidth=4).grid(row=2, column=3)
but7 = Button(text="7", bg="white", fg="black", font="comic 11 bold", height=4, width=6, borderwidth=4).grid(row=3, column=1)
but8 = Button(text="8", bg="white", fg="black", font="comic 11 bold", height=4, width=6, borderwidth=4).grid(row=3, column=2)
but9 = Button(text="9", bg="white", fg="black", font="comic 11 bold", height=4, width=6, borderwidth=4).grid(row=3, column=3)
but0 = Button(text="0", bg="white", fg="black", font="comic 11 bold", height=4, width=6, borderwidth=4).grid(row=4, column=1)

first = IntVar()

al.mainloop()
