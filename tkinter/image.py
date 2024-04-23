import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def resize_image(event):
    global background_tk
    width = event.width
    height = event.height
    new_background = background.resize((width, height))
    background_tk = ImageTk.PhotoImage(new_background)
    canvas.create_image(0, 0, image=background_tk, anchor='nw')


screen = tk.Tk()
screen.title("Adding image to our project")
screen.geometry("500x500")

insta_original = Image.open("insta.jpg").resize((30,30))
instaTk = ImageTk.PhotoImage(insta_original)
# Labels, Buttons, tk.Canvas are the only widgets which accepts images.
# ttk.Label(screen, image=instaTk).pack()
# ttk.Button(screen, text="Click me", image=instaTk, compound="left").pack(pady=10)

background = Image.open("insta.jpg").resize((500,500))
background_tk = ImageTk.PhotoImage(background)
canvas = tk.Canvas(screen)
canvas.pack(expand=True, fill='both')
canvas.create_image(0,0, image=background_tk, anchor='nw')
canvas.bind('<Configure>', resize_image)

screen.mainloop()
