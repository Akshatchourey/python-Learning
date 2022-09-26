from tkinter import *
from PIL import Image, ImageTk

al = Tk()
al.geometry("980x600")
al.title("Python with akshat")

f1 = Frame(al, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)
Label(f1, text="Beaker section", fg="red", font="comic 12 bold").grid(pady=305)
f2 = Frame(al, bg="grey", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill=X)
Label(f2, text="nemkin section", fg="red", font="comic 25 bold").grid(padx=280)
f3 = Frame(al)
f3.pack()


def danger():
    ak = Tk()
    ak.geometry("355x555")
    f5 = Frame(ak, borderwidth=10)
    f5.pack(side=LEFT)
    Label(ak, text="Generated Bill", font="comic 25 bold").pack()
    Label(f5, text="|\n"*30).pack(pady=14)
    f6 = Frame(ak, borderwidth=10)
    f6.pack(side=RIGHT)
    Label(f6, text="|\n"*30).pack(pady=14)
    totle = (5 * fval.get()) + (10 * sval.get()) + (20 * tval.get()) + (30 * foval.get()) + (100 * fival.get()) + (
                800 * sival.get())
    f7 = Frame(ak)
    f7.pack(side=LEFT)
    Label(f7, text="NAME", font="comic 25 bold").pack()
    Label(f7, text="1.parlay\n2.bitania\n3.gooday\n4.crackjeck\n5.Motalal\n6.yAkshat Namkines", font="comic 10 bold").pack()
    f8 = Frame(ak)
    f8.pack(side=LEFT)
    Label(f8, text="No.       Rs.", font="comic 25 bold").pack()
    Label(f8, text=f"{fval.get()}\t\t{5 * fval.get()}\n{sval.get()}\t\t{10 * sval.get()}\n{tval.get()}\t\t{20 * tval.get()}\n{foval.get()}\t\t{30 * foval.get()}\n{fival.get()}\t\t{100 * fival.get()}\n{sival.get()}\t\t{800 * sival.get()}\nTOTLE\t\t{totle}", font="comic 10 bold").pack()
    mainloop()


Label(f3, text="Welcom To My Shop", font="comic 20 bold").grid()
fir = Label(f3, text="\f1.parlay = 5Rs", font="comic 10 bold").grid()
sec = Label(f3, text="2.bitania = 10Rs", font="comic 10 bold").grid()
thi = Label(f3, text="3.gooday = 20Rs", font="comic 10 bold").grid()
fo = Label(f3, text=" 4.crackjeck =30Rs", font="comic 10 bold").grid()
fif = Label(f3, text="\f5.Motalal=100Rs", font="comic 10 bold").grid()
sic = Label(f3, text=" 6.Akshat Namkines=800Rs", font="comic 10 bold").grid()

fval = IntVar()
sval = IntVar()
tval = IntVar()
foval = IntVar()
fival = IntVar()
sival = IntVar()
pree = IntVar()

fint = Entry(f3, textvariable=fval).grid(row=1, column=2)
sint = Entry(f3, textvariable=sval).grid(row=2, column=2)
tint = Entry(f3, textvariable=tval).grid(row=3, column=2)
foint = Entry(f3, textvariable=foval).grid(row=4, column=2)
fiint = Entry(f3, textvariable=fival).grid(row=5, column=2)
siint = Entry(f3, textvariable=sival).grid(row=6, column=2)
preeint = Checkbutton(f3, text="want to prebook your meal?").grid(row=7, column=2)

button = Button(f3, text="Generate Bill.", bg="blue", fg="black", font="comic 10 bold", command=danger).grid()
image = Image.open("ak1.png")
photo = ImageTk.PhotoImage(image)
Label(image=photo).pack()

al.mainloop()
