from tkinter import *
import os
import sqlite3 as base
data_base = base.connect("demo1.db")
cursor = data_base.cursor()

register_page =Tk()
register_page.title("KM bank")
register_page.configure(bg="#fdb9b9")
register_page.iconbitmap("dbmsicon.ico")
#register_page.geometry("900x700")


account_page_exists=0


cursor.execute("SELECT cust_id_g FROM customerID_generator where row =1")
x = cursor.fetchall()
cust_id_ =x[0][0]
print(cust_id_)
cursor.execute("UPDATE customerID_generator SET cust_id_g = :cust_id_d WHERE row=1;",{
    'cust_id_d':x[0][0]+1
    }
    )
##########################################################################
# Only functions()
def register_button():
    full_name =  full_name_box.get()
    street =     street_box.get()
    state =      state_box.get()
    city =       city_box.get()
    pin =        pin_box.get()
    dob =        dob_box.get()
    age =        age_box.get()
    gender=      gender_box.get()
    email  =     email_box.get()
    Contact =    Contact_box.get()
    pan=         pan_box.get()
    nationality= nationality_box.get()
    password=    password_box.get()
    re_password= re_password_box.get()
    if full_name =='':
        lab = Label(register_page,text ="Please enter Full name",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)
    elif street =='':
        lab = Label(register_page,text ="Please enter street",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
    elif state =='':
        lab = Label(register_page,text ="Please enter state",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
    elif city =='':
        lab = Label(register_page,text ="Please enter city",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
    elif pin =='':
        lab = Label(register_page,text ="Please enter pin",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
    elif dob =='':
        lab = Label(register_page,text ="Please enter dob",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
    elif age =='':
        lab = Label(register_page,text ="Please enter age",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
    elif gender =='':
        lab = Label(register_page,text ="Please enter gender",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
    elif email =='':
        lab = Label(register_page,text ="Please enter email",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
    elif Contact =='':
        lab = Label(register_page,text ="Please enter Contact",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
    elif pan =='':
        lab = Label(register_page,text ="Please enter pan",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
    elif nationality =='':
        lab = Label(register_page,text ="Please enter nationality",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
    elif password =='':
        lab = Label(register_page,text ="Please enter password",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
    elif re_password =='':
        lab = Label(register_page,text ="Please re-enter password",font="Android 15",padx=10,pady=10)
        lab.grid(row=19,column=1)        
     
    elif password != re_password:
        Label(register_page,text="Password mismatch",font ="none 15",bg ="#fdb9b9").grid(row=16,column=2,pady=10,padx=20,sticky = W)
    else:

        cursor.execute("INSERT INTO CUSTOMER VALUES (:CUST_ID,:password,:NAME, :DOB, :AGE,:GENDER,:EMAIL,:Contact,:pan,:nationality)",
               {
                   
                   'CUST_ID':cust_id_,
                   'password':password,
                   'NAME': full_name,
                   'DOB':dob ,
                   'AGE':age ,
                   'GENDER':gender ,
                   'EMAIL': email,
                   'Contact':Contact ,
                   'pan': pan,
                   'nationality':nationality 
                })
        cursor.execute("INSERT INTO CUSTOMER_address VALUES (:CUST_ID, :STREET,:CITY,:STATE,:PIN)",
                {
                    'CUST_ID':cust_id_,
                    'STREET':street,
                    'STATE':state ,
                    'CITY':city ,
                    'PIN':pin
                })
        create_account_after_register()    
        




               
def go_back_button():
    register_page.destroy()

##########################################################################
#Only Label()
#Should code to generate Cust_id for each customer which is not done yet
cust_id=Label(register_page,text = "Customer ID",font ="none 15",bg ="#fdb9b9")
cust_id_display=Label(register_page,text = cust_id_,font ="none 15",bg ="#fdb9b9")
full_name=Label(register_page,text = "Full name",font ="none 15",bg ="#fdb9b9")
#address=Label(register_page,text="Address",font ="none 15",bg ="#fdb9b9")
street=Label(register_page,text = "Address: Street",font ="none 15",bg ="#fdb9b9")
state=Label(register_page,text="Address: State",font ="none 15",bg ="#fdb9b9")
city=Label(register_page,text = "Address: City",font ="none 15",bg ="#fdb9b9")
pin=Label(register_page,text = "Address: pin",font ="none 15",bg ="#fdb9b9")
dob=Label(register_page,text="DOB",font ="none 15",bg ="#fdb9b9")
age=Label(register_page,text = "Age",font ="none 15",bg ="#fdb9b9")
gender=Label(register_page,text="gender",font ="none 15",bg ="#fdb9b9")
email=Label(register_page,text = "Email ID",font ="none 15",bg ="#fdb9b9")
Contact=Label(register_page,text="Contact",font ="none 15",bg ="#fdb9b9")
pan=Label(register_page,text = "PAN no.",font ="none 15",bg ="#fdb9b9")
nationality=Label(register_page,text="Nationality",font ="none 15",bg ="#fdb9b9")
password=Label(register_page,text="Password",font ="none 15",bg ="#fdb9b9")
repassword=Label(register_page,text="re-enter Password",font ="none 15",bg ="#fdb9b9")
##########################################################################
#Only Entry() 
#cust_id=Entry(register_page,text = "Customer ID",font ="none 15",bg ="#fdb9b9")
full_name_box=Entry(register_page,text = "Full name",font ="none 15",bg ="#fdb9b9")

street_box=Entry(register_page,text = "Street",font ="none 15",bg ="#fdb9b9")
state_box=Entry(register_page,text="State",font ="none 15",bg ="#fdb9b9")
city_box=Entry(register_page,text = "City",font ="none 15",bg ="#fdb9b9")
pin_box=Entry(register_page,text = "Pin",font ="none 15",bg ="#fdb9b9")
dob_box=Entry(register_page,text="DOB",font ="none 15",bg ="#fdb9b9")
age_box=Entry(register_page,text = "Age",font ="none 15",bg ="#fdb9b9")
gender_box=Entry(register_page,text="gender",font ="none 15",bg ="#fdb9b9")
email_box=Entry(register_page,text = "Email ID",font ="none 15",bg ="#fdb9b9")
Contact_box=Entry(register_page,text="Contact",font ="none 15",bg ="#fdb9b9")
pan_box=Entry(register_page,text = "PAN no.",font ="none 15",bg ="#fdb9b9")
nationality_box=Entry(register_page,text="Nationality",font ="none 15",bg ="#fdb9b9")
password_box=Entry(register_page,font="none 15", w=20,show="*",bg ="#fdb9b9")
re_password_box=Entry(register_page,font="none 15", w=20,show="*",bg ="#fdb9b9")
##########################################################################
#Only Buttons()
register=Button(register_page,text="Register",padx=30,pady=5,command=register_button)
go_back=Button(register_page,text="Go Back to login",padx=30,pady=5,command=go_back_button)
##########################################################################
#GRID()
##########################################################################
#Only Label.grid()
cust_id.    grid(row=1,column=0,pady=10,padx=20,sticky = W)
cust_id_display.    grid(row=1,column=1,pady=10,padx=20,sticky = W)
full_name.  grid(row=2,column=0,pady=10,padx=20,sticky = W)
street.     grid(row=4,column=0,pady=10,padx=20,sticky = W)
state.      grid(row=5,column=0,pady=10,padx=20,sticky = W)
city.       grid(row=6,column=0,pady=10,padx=20,sticky = W)
pin.        grid(row=7,column=0,pady=10,padx=20,sticky = W)
dob.        grid(row=8,column=0,pady=10,padx=20,sticky = W)
age.        grid(row=9,column=0,pady=10,padx=20,sticky = W)
gender.     grid(row=10,column=0,pady=10,padx=20,sticky = W)
email.      grid(row=11,column=0,pady=10,padx=20,sticky = W)
Contact.    grid(row=12,column=0,pady=10,padx=20,sticky = W)
pan.        grid(row=13,column=0,pady=10,padx=20,sticky = W)
nationality.grid(row=14,column=0,pady=10,padx=20,sticky = W)
password.   grid(row=15,column=0,pady=10,padx=20,sticky = W)
repassword  .grid(row=16,column=0,pady=10,padx=20,sticky = W)
##########################################################################
#Only Entry.grid()
#cust_id_box.    grid(row=1,column=1,pady=10,padx=20,sticky = W)
full_name_box.  grid(row=2,column=1,pady=10,padx=20,sticky = W)
street_box.     grid(row=4,column=1,pady=10,padx=20,sticky = W)
state_box.      grid(row=5,column=1,pady=10,padx=20,sticky = W)
city_box.       grid(row=6,column=1,pady=10,padx=20,sticky = W)
pin_box.        grid(row=7,column=1,pady=10,padx=20,sticky = W)
dob_box.        grid(row=8,column=1,pady=10,padx=20,sticky = W)
age_box.        grid(row=9,column=1,pady=10,padx=20,sticky = W)
gender_box.     grid(row=10,column=1,pady=10,padx=20,sticky = W)
email_box.      grid(row=11,column=1,pady=10,padx=20,sticky = W)
Contact_box.    grid(row=12,column=1,pady=10,padx=20,sticky = W)
pan_box.        grid(row=13,column=1,pady=10,padx=20,sticky = W)
nationality_box.grid(row=14,column=1,pady=10,padx=20,sticky = W)
password_box.   grid(row=15,column=1,pady=10,padx=20,sticky = W)
re_password_box.grid(row=16,column=1,pady=10,padx=20,sticky = W)
##########################################################################
# Only Button.grid()
register.grid(row=17,column=1,pady=10,padx=20,sticky = W)
go_back.grid(row=18,column=1,pady=10,padx=20,sticky = W)
###############################################################################################################
###############################################################################################################
#Account Part
def create_account_after_register():
    account_page = Toplevel()
    account_page.title("KM bank")
    account_page.configure(bg="#fdb9b9")
    account_page.iconbitmap("dbmsicon.ico")
    cursor.execute("SELECT acc_no_g FROM account_NO_generator where row =1")
    x = cursor.fetchall()
    acc_no =x[0][0]
    print(acc_no)
    cursor.execute("UPDATE account_NO_generator SET acc_no_g = :acc_no WHERE row=1;",{
    'acc_no':x[0][0]+1
        }
        )
    #Account Labels
    acc_no_l=Label(account_page,text = "Account No.",font ="none 15",bg ="#fdb9b9")
    acc_no_d=Label(account_page,text = acc_no,font ="none 15",bg ="#fdb9b9")

    #Label.grid()
    acc_no_l.    grid(row=1,column=0,pady=10,padx=20,sticky = W)
    acc_no_d.    grid(row=1,column=1,pady=10,padx=20,sticky = W)









##########################################################################
mainloop()
data_base.commit()
data_base.close()