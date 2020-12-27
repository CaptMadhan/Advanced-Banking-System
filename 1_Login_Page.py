from tkinter import *
import sqlite3 as base
# create or connect a data base
data_base = base.connect("demo1.db")
# create a cursor
cursor = data_base.cursor()

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
    user_i= username_box.get()
    passw_i=password_box.get()
    cursor.execute("SELECT PASSWORD from customer WHERE CUST_ID = :CUSTID;",{ 'CUSTID':user_i})
    x = cursor.fetchall()
    
    if user_i =='':
        lab = Label(login_page,text ="Please enter Cust_ID",font="Android 15",padx=10,pady=10)
        lab.grid(row=5,column=1)
    elif passw_i =='':
        lab = Label(login_page,text ="Please enter Password",font="Android 15",padx=10,pady=10)
        lab.grid(row=5,column=1,columnspan=2)       
    elif user_i == u and passw_i == p:
        text = "hello "+user_i
        lab = Label(login_page,text = text,font="Android 15",padx=10,pady=10)
        lab.grid(row=5,column=1,columnspan=2)
    elif x[0][0]:
        cursor.execute("SELECT NAME from customer WHERE CUST_ID = :CUSTID;",{ 'CUSTID':user_i})
        n = cursor.fetchall()
        print(x[0][0])
        passw_i == x[0][0]
        text = "hello "+ n[0][0]
        lab = Label(login_page,text = text,font="Android 15",padx=10,pady=10)
        lab.grid(row=5,column=1,columnspan=2)
        
    else:
        lab = Label(login_page,text ="Try Again",font="Android 20",padx=10,pady=10)
        lab.grid(row=5,column=1,columnspan=2)
def signup():
    return

##########################################################################
#Only Label()
#picture = PhotoImage(file = "")
#lab = Label(login_page, image=picture)
#lab.grid(row=0,column=0,columnspan=2)
username=Label(login_page,text = "CustomerID",font ="none 15",bg ="#fdb9b9")
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
data_base.commit()
data_base.close()