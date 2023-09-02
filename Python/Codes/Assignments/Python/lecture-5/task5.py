import tkinter as tk
def led_on():
    c.itemconfig(circle,fill='red')

def led_off():
    c.itemconfig(circle,fill='white')

win=tk.Tk()
c=tk.Canvas(win,width=500,height=500)
c.pack()
circle=c.create_oval(100,100,400,400,fill='white')
b1=tk.Button(win,text='ON',command=led_on)
b2=tk.Button(win,text='OFF',command=led_off)
c.pack()
b1.pack()
b2.pack()
win.mainloop()