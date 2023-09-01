import tkinter
def b1():
    print("Ahmed")
def b2():
    print("hamada")
def b3():
    print("Youssef")
def b4():
    print("samy")
    
win=tkinter.Tk()    
win.title("Buttons")
win.geometry("500x200+100+100")
win.resizable(True,True)
button1=tkinter.Button(win,text="B1",command=b1).grid(row=0,column=1)
button2=tkinter.Button(win,text="B2",command=b2).grid(row=1,column=0)
button3=tkinter.Button(win,text="B3",command=b3).grid(row=1,column=2)
button4=tkinter.Button(win,text="B4",command=b4).grid(row=2,column=1)
win.mainloop()

