import tkinter as tk
def operation():
    if v.get()==1:
        tk.Label(m,text=str(int(e1.get())+int(e2.get()))).grid(row=2,column=2)
    else:
        tk.Label(m,text=str(int(e1.get())-int(e2.get()))).grid(row=2,column=2)
        
m=tk.Tk()
v=tk.IntVar()
tk.Button(m,text="calculate",command=operation).grid(row=3,column=3)
l1=tk.Label(m,text="Enter the value M").grid(row=0,column=0)
l2=tk.Label(m,text="Enter the value N").grid(row=1,column=0)
r1=tk.Radiobutton(m,text="SUM",variable=v,value=1).grid(row=4,column=0)
r2=tk.Radiobutton(m,text="SUB",variable=v,value=2).grid(row=5,column=0)
e1=tk.Entry(m)
e2=tk.Entry(m)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
m.mainloop()

