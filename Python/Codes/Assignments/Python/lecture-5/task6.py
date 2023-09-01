import tkinter as tk
import math
def operation():
    tk.Label(m,text=str(math.factorial (int(e.get())))).grid(row=1,column=1)

m=tk.Tk()
e=tk.Entry(m)
l=tk.Label(m,text="Enter Value N:")
b=tk.Button(m,text="calc",command=operation)
l.grid(row=0,column=0)
e.grid(row=0,column=1)
b.grid(row=2,column=2)
m.mainloop()