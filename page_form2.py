"""from tkinter import *
al = Tk()

al.title("Python with akshat")
al.geometry("790x535")
button = Button(text="Theory", bg="blue", fg="black")
button.pack(side=TOP, anchor="ne", fill=X)
f1 = Frame(al, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, anchor="nw", fill=Y)
ti = Label(f1, text="Book section", fg="red")
ti.pack(pady=145)
# relif-border styling=SUNKEN, RATSED, GROOVE, RIDGE.
akshat = Label(text='''n the first superstring revolution in 1984, \nmany physicists turned to string theory as a 
unified theory of particle physics and quantum gravity.\n Unlike supergravity theory string theory\n was able to 
accommodate the chirality \nof the standard model, and it provided a theory \nof gravity consistent with quantum 
effects.Another feature\n of string theory that many physicists were\n drawn to in the 1980s and 1990s was its high 
degree of uniqueness.''', bg='yellow', fg='red', font="comics 19 bold", padx=0, pady=50, borderwidth=25, relief=GROOVE,)
akshat.pack(side=TOP, anchor="ne")
al.mainloop()"""

from tkinter import *
al = Tk()
al.geometry("765x445")
username = Label(text="username").grid()
password = Label(text="password").grid()


def getvals():
    print(f"user name is={uservalue.get()}")
    print(f"password is={passvalue.get()}")


# variable class in tkinter
# BooleanVar, IntVar, StringVar, DoubleVar
uservalue = StringVar()
passvalue = StringVar()
userentry = Entry(al, textvariable=uservalue)
passentry = Entry(al, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
button = Button(text="summit", command=getvals).grid()
al.mainloop()
