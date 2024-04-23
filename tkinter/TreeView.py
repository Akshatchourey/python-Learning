import tkinter as tk
from tkinter import ttk
from random import choice,randint

sc = tk.Tk()
sc.geometry('600x400')

first_name = ['akshat','kanika','anjali','satish','naman']
last_name = ['chourey','pare','singh','sharma','roy']
table = ttk.Treeview(sc, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='First Name')
table.heading('last', text='Surname')
table.heading('email', text='Email')
table.pack(fill = 'both', expand = True)


for i in range(30):
    name = choice(first_name)
    surname = choice(last_name)
    email = f"{surname}{randint(1,100)}@gmail.com"
    row = (name, surname, email)
    table.insert(parent='', index=0, values=row, tags=('tag_colour',))

table.tag_configure("tag_colour", foreground="red")

def item_select():
    for i in table.selection():
        print(table.item(i)['values'])

def delete_item():
    for i in table.selection():
        table.delete(i)


table.bind('<<TreeviewSelect>>', lambda event:item_select())
table.bind('<Delete>', lambda event:delete_item())

sc.mainloop()
