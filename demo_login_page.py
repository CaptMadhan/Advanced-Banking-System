from tkinter import *

root =Tk()
root.title("Instagram")
root.configure(bg="#fdb9b9")
root.iconbitmap("dbmsicon.ico")
root.geometry("400x500")

def log():
    user= username_box.get()
    passw=password_box.get()
    u="admin"
    p="1234"
    if user == u and passw == p:
        text = "hello "+user
        lab = Label(root,text = text,font="Android 20",padx=10,pady=10)
        lab.grid(row=4,column=0,columnspan=2)
    else:
        lab = Label(root,text ="Try Again",font="Android 20",padx=10,pady=10)
        lab.grid(row=4,column=0,columnspan=2)


#picture = PhotoImage(file = "")
#lab = Label(root, image=picture)
#lab.grid(row=0,column=0,columnspan=2)
username=Label(root,text = "Username",font ="none 15",bg ="#fdb9b9")
password=Label(root,text="Password",font ="none 15",bg ="#fdb9b9")
username_box=Entry(root,font="none 15", w=20)
password_box=Entry(root,font="none 15", w=20,show="*")
login=Button(root,text="Login",padx=30,pady=5,command=log)


username.grid(row=1,column=0,pady=10,padx=20)
password.grid(row=2,column=0,pady=5,padx=20)
username_box.grid(row=1,column=1,pady=10,padx=20)
password_box.grid(row=2,column=1,pady=10,padx=20)
login.grid(row=3,column=0,columnspan=2,pady=10)


root.mainloop()