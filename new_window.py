from tkinter import *

root =Tk()
root.title("Instagram")
root.configure(bg="#fdb9b9")
root.iconbitmap("dbmsicon.ico")
root.geometry("400x500")


string = "hello"
b=0
def create():
    global b
    global new
    if b == 0:    
        new = Toplevel()
        new.title("Instagram")
        new.configure(bg="#fdb9b9")
        new.iconbitmap("dbmsicon.ico")
        new.geometry("300x500")

        lab = Label(new,text="hello")
        lab.pack()
    if new.winfo_exists():
        b=1
    else:
        new = Toplevel()
        new.title("Instagram")
        new.configure(bg="#fdb9b9")
        new.iconbitmap("dbmsicon.ico")
        new.geometry("300x500")
        lab = Label(new,text="hello")
        lab.pack()
        b=1

butt = Button(root,text ="ADD",font ="none 25",padx=20,pady=10,command=create)
butt.pack(pady=40)

mainloop()