import sys
from tkinter import *
import tkinter as tk
def box():
    from tkinter import messagebox
    UName = var1.get()
    PWD = var2.get()
    USERNAME = "user"
    PASSWORD = "user"
    if UName!="" and PWD!="" and UName!=USERNAME:
        messagebox.showwarning("LOGIN FAIL","USERNAME IS INCORRECT")
    elif PWD!="" and PWD!="" and PWD!=PASSWORD:
        messagebox.showwarning("LOGIN FAIL","PASSWORD IS INCORRECT")
    else:
        messagebox.showinfo("WELCOME","WELCOME")
        top.withdraw()
        import user

def clear():
    var11 = StringVar()#declaring the variable to store the text
    var22 = StringVar()
    e1 = Entry(top,textvariable= var11).place(x = 550, y = 250)
    e2 = Entry(top,textvariable = var22,show="*").place(x = 550, y = 320)
top= Tk()

image1 = tk.PhotoImage(file='bg1.png')
w = image1.width()
h = image1.height()
top.geometry("%dx%d+0+0" % (w, h))
panel1 = tk.Label(top, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
panel1.image = image1

var1 = StringVar()#declaring the variable to store the text
var2 = StringVar()#.....\....\...
top.title("LOGIN IN AS CUSTOMER")


name = Label(top, text = "Login",font="Algerian 30 bold",background="white").place(x = 50,y = 50)
name = Label(top, text = "Login User Name:",font = 'Algerian 15 bold',background = "black",fg = "white").place(x = 50,y = 250)
nick = Label(top, text = "Password:",font = 'Algerian 15 bold',background = "black",fg = "white").place(x = 50,y = 320)
resetbtn = Button(top, text = "   Reset   ",command =clear,font='HarlowSolidItalic 14 bold italic',background = "dark blue",foreground="white" ).place(x = 50, y = 500)
sbmitbtn = Button(top, text = " Continue ",command = box,font='HarlowSolidItalic 14 bold italic',background = "dark blue",foreground="white").place(x = 600, y = 500)

large_font = ('Algerian 16')
e1 = Entry(top,textvariable= var1,font = large_font).place(x = 300, y = 250)
e2 = Entry(top,textvariable = var2,show="*",font = large_font).place(x = 300, y = 320)

top.mainloop()
