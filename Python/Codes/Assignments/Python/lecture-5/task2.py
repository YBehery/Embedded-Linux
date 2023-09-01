import tkinter as tk
def reverse():
    tk.Label(m,text=e.get()[::-1]).grid(row=1,column=0)

m=tk.Tk()
tk.Label(m,text="Enter a word:").grid(row=0,column=0)
e=tk.Entry(m)
e.grid(row=0,column=1)
tk.Button(m,text="Validate",command=reverse).grid(row=3,column=3)
m.mainloop()