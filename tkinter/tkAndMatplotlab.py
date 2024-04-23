import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graph1():
    dates = ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01']
    values = [20, 40, 10, 50, 25]
    plt.plot(dates, values, label='Line 1')
    canvas.draw()

def graph2():
    dates = ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01']
    values = [10, 30, 20, 40, 10]
    plt.plot(dates, values, label='Line 2')
    plt.set_title("Graph")
    plt.set_xlabel("Entries")
    plt.set_ylabel("Amount")
    plt.legend()
    canvas.draw()

def clear_graph():
    global plt
    fig.clf()
    plt = fig.add_subplot(111)
    canvas.draw()


sc = tk.Tk()
fig = Figure(figsize=(7, 5), dpi=110)
canvas = FigureCanvasTkAgg(fig, master=sc)
canvas.get_tk_widget().pack()
plt = fig.add_subplot(111)


tk.Button(sc, command=lambda: clear_graph(), text="clear Graph").pack()
tk.Button(sc, command=lambda: graph1(), text="Create Graph").pack()
tk.Button(sc, command=lambda: graph2(), text="Create Graph").pack()


sc.mainloop()
