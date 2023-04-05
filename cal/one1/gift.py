from tkinter import *
import random
from PIL import Image, ImageTk

al = Tk()
al.geometry("1500x800")
al.title("Chourey's Gift Box.")


def out():
    a = random.randint(1, 5)
    if a == 1:
        aks = "1.jpg"
    elif a == 2:
        aks = "4.jpg"
    else:
        aks = "5.jpg"
    image = Image.open(aks)
    pho = ImageTk.PhotoImage(image)
    Label(image=pho).pack()


Button(text="Generate Gift.", command=out).pack()
al.mainloop()
