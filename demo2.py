from tkinter import *

root =Tk()
root.title("APP")
root.configure(bg="#263d42")
root.iconbitmap("dbmsicon.ico")
root.geometry("500x500")

def click1():
    text1 = input1.get()
    global lab1
    lab1 = Label(root, text = text1)
    lab1.grid(pady = 0)
def clear():
    lab1.destroy()

text = Label(root, text = "Say hi", font="Algerian 15",bg="#263d42",fg ="white", padx=10, pady=10)
input1 = Entry(root, font = "none 15", w=20)
but1 = Button(root,text = "click me",bg ="white",fg = "red", font="Algerian 20",command=click1)
clear = Button(root, text="Clear",bg ="white",fg = "red", font="Algerian 20",command=clear)

text.grid(row=0, column=0,padx=10,pady=10)
input1.grid(row=0, column=1,padx=10,pady=10)
but1.grid(row=1,column=0,columnspan=1,padx = 20)
clear.grid(row=1,column=1,columnspan=2,padx=10)
root.mainloop()