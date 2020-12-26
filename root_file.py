from tkinter import *
import register_page
import os

login_page =Tk()
login_page.title("KM bank")
login_page.configure(bg="#fdb9b9")
login_page.iconbitmap("dbmsicon.ico")
#login_page.geometry("900x700")

##########################################################################
# Only functions()
def login():
    u="admin"
    p="1234"
    user= username_box.get()
    passw=password_box.get()
    if user == u and passw == p:
        text = "hello "+user
        lab = Label(login_page,text = text,font="Android 20",padx=10,pady=10)
        lab.grid(row=4,column=0,columnspan=2)
    else:
        lab = Label(login_page,text ="Try Again",font="Android 20",padx=10,pady=10)
        lab.grid(row=4,column=0,columnspan=2)
register_page_exists=0
def signup():
    global register_page_exists
    global register_page
    if register_page_exists == 0:    
        os.system('register_page.py')

    if register_page.register_page.winfo_exists():
        register_page_exists=1
    else:
        os.system('register_page.py')
        register_page_exists=1

##########################################################################
#Only Label()
#picture = PhotoImage(file = "")
#lab = Label(login_page, image=picture)
#lab.grid(row=0,column=0,columnspan=2)
username=Label(login_page,text = "Username",font ="none 15",bg ="#fdb9b9")
password=Label(login_page,text="Password",font ="none 15",bg ="#fdb9b9")
##########################################################################

#Only Entry() 
username_box=Entry(login_page,font="none 15", w=20)
password_box=Entry(login_page,font="none 15", w=20,show="*")
##########################################################################

#Only Buttons()
login=Button(login_page,text="Login",padx=20,pady=3,command=login)
sign_up=Button(login_page,text="SignUp",padx=20,pady=3,command=signup)
##########################################################################
#GRID()
##########################################################################
#Only Label.grid()
username.grid(row=1,column=0,pady=10,padx=20)
password.grid(row=2,column=0,pady=5,padx=2)
##########################################################################
#Only Entry.grid()
username_box.grid(row=1,column=1,pady=10,padx=20)
password_box.grid(row=2,column=1,pady=10,padx=20)
##########################################################################
# Only Button.grid()
login.grid(row=3,column=1,pady=8,padx=20,sticky = W)
sign_up.grid(row=4,column=1,pady=8,padx=20,sticky = W)

login_page.mainloop()