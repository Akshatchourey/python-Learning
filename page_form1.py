from tkinter import *
from PIL import Image, ImageTk
import turtle
a = turtle.Turtle()
ak = Tk()
# Geometry
ak.geometry("644x434")
'''ak.minsize(200, 150)
ak.maxsize(800, 750)'''
# Jpg image
'''
image = Image.open("since.py.jpg")
photo = ImageTk.PhotoImage(image)
variable = Label(image=photo)
variable.pack()'''

button = Button(ak, text="good morning", bg='gray', fg='red')
button.pack()
frame = Frame(ak, bg='blue')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

heading = Label(text="I love Python GUI.")
heading.pack()

a.color("red", 'orange')

a.speed(10)

a.begin_fill()
for i in range(73):
    a.forward(250)
    a.left(143)
    a.end_fill()
a.penup()
a.backward(300)
a.pendown()
a.begin_fill()
for i in range(130):
    a.forward(250)
    a.left(166)
    a.end_fill()


turtle.done()
ak.mainloop()
