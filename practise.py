from tkinter import *

root =Tk()
root.title("APP")
root.configure(bg="#365d32")
root.iconbitmap("dbmsicon.ico")
root.geometry("500x500")

def click():
    lab = Label(root, text = "hello")
    lab.pack(pady = 0)

def click1():
    text1 = ent.get()
    lab1 = Label(root, text = text1)
    lab1.pack(pady = 0)

lab = Label(root, text ="Hii hello howdy",bg="#365d32",fg ="white",font="Algerian 40", pady = 10)
lab.pack()

ent = Entry(root, w=30, font ="none 22")
ent.pack(pady=10)
 
but1 = Button(root,text = "click me",bg ="white",fg = "red", font="Algerian 20",command=click1)
but1.pack()

but = Button(root,text = "click me",bg ="white",fg = "red", font="Algerian 20",command=click)
but.pack(pady=60)
root.mainloop()
