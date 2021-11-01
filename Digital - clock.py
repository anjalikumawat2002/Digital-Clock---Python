from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('clock')
def time():
    string = strftime(" %r")
    lbl.config(text = string)
    lbl.after(1000,time)

lbl = Label(root,font=('calibri',150,'bold'),
            background ='black',
            foreground ='white')
lbl.pack(anchor = 'center')
time()
mainloop()
