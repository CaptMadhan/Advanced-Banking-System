from tkinter import *
import os
import sqlite3 as base
import datetime
# create or connect a data base
data_base = base.connect("demo1.db")
# create a cursor
cursor = data_base.cursor()

'''
cursor.execute("select * from account ")
print(cursor.fetchall())
cursor.execute("select * from transactions where ac_no=:ac_no ",{'ac_no':66556655063})
x = cursor.fetchall()
print(x)
'''
#cursor.execute("SELECT * FROM transactions where ac_no =:ac_no",{'ac_no':ac_no}")
#print(cursor.fetchall())
'''
cursor.execute("SELECT * FROM transactions where ac_no =:ac_no",{'ac_no':66556655059})
transactions = cursor.fetchall()
if not len(transactions):
    print("No transactions")
else:
    print(transactions)
'''
#ac_no = 66556655059
#cursor.execute("select * FROM transactions where ac_no =:ac_no",{'ac_no':ac_no})
#x = cursor.fetchall()
#print(x)

add_emp_page =Tk()
add_emp_page.title("KM bank")
add_emp_page.configure(bg="#fdb9b9")
add_emp_page.iconbitmap("dbmsicon.ico")

#functions only
def go_back_button():
    add_emp_page.destroy()
def register_button():
    branch_id =     branch_id_e.get()
    name =          name_e.get()
    street =     street_box.get()
    state =      state_box.get()
    city =       city_box.get()
    pin =        pin_box.get()
    email =         email_e.get()
    gender =        gender_e.get()
    contact =       contact_e.get()
    nationality=    nationality_e.get()
    dob=            dob_e.get()
    username  =     username_e.get()
    password =    password_e.get()
    if branch_id =='':
        Label(add_emp_page,text ="Please enter Branch_id",font="Android 15",padx=10,pady=10)    .grid(row=17,column=1)
    elif name =='':
        Label(add_emp_page,text ="Please enter Name",font="Android 15",padx=10,pady=10)         .grid(row=17,column=1)
    elif email =='':
        Label(add_emp_page,text ="Please enter Email",font="Android 15",padx=10,pady=10)        .grid(row=17,column=1)
    elif street =='':
        Label(add_emp_page,text ="Please enter street",font="Android 15",padx=10,pady=10)      .grid(row=17,column=1)        
    elif state =='':
        Label(add_emp_page,text ="Please enter state",font="Android 15",padx=10,pady=10)       .grid(row=17,column=1)        
    elif city =='':
        Label(add_emp_page,text ="Please enter city",font="Android 15",padx=10,pady=10)        .grid(row=17,column=1)        
    elif pin =='':
        Label(add_emp_page,text ="Please enter pin",font="Android 15",padx=10,pady=10)         .grid(row=17,column=1)        
    elif gender =='':
        Label(add_emp_page,text ="Please enter Gender",font="Android 15",padx=10,pady=10)       .grid(row=17,column=1)
    elif contact =='':
        Label(add_emp_page,text ="Please enter Contact No.",font="Android 15",padx=10,pady=10)  .grid(row=17,column=1)
    elif nationality =='':
        Label(add_emp_page,text ="Please enter Nationality",font="Android 15",padx=10,pady=10)  .grid(row=17,column=1)
    elif dob =='':
        Label(add_emp_page,text ="Please enter dob",font="Android 15",padx=10,pady=10)      .grid(row=17,column=1)
    elif username =='':
        Label(add_emp_page,text ="Please enter username",font="Android 15",padx=10,pady=10) .grid(row=17,column=1)
    elif password =='':
        Label(add_emp_page,text ="Please enter password",font="Android 15",padx=10,pady=10) .grid(row=17,column=1)
    else:
        cursor.execute("INSERT INTO OFFICER VALUES (:EMP_ID ,:BRANCH_ID , :NAME , :EMAIL ,:GENDER  ,:CONTACT ,:NATIONALITY ,:DOB ,:USERNAME ,:PASSWORD )",
               {
                   'EMP_ID':emp_id,
                   'BRANCH_ID': branch_id,
                   'NAME':name ,
                   'EMAIL':email ,
                   'GENDER':gender ,
                   'CONTACT': contact,
                   'NATIONALITY':nationality ,
                   'DOB': dob,
                   'USERNAME':username,
                   'PASSWORD':password 
                })
        cursor.execute("INSERT INTO OFFICER_ADDRESS VALUES (:EMP_ID , :STREET  ,:CITY,:STATE,:PIN)",
                {
                    'EMP_ID':emp_id,
                    'STREET':street,
                    'STATE':state ,
                    'CITY':city ,
                    'PIN':pin
                })
        add_emp_page.destroy()

cursor.execute("SELECT employee_id_g FROM employeeID_generator where row =1")
x = cursor.fetchall()
emp_id =x[0][0]
cursor.execute("UPDATE employeeID_generator SET employee_id_g = :employee_id_g WHERE row=1;",{
    'employee_id_g':x[0][0]+1
    }
    )    
#Labels
Label(add_emp_page,text = "EMP_ID",font ="none 15",bg ="#fdb9b9")       .grid(row=1,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text = emp_id,font ="none 15",bg ="#fdb9b9")         .grid(row=1,column=1,pady=10,padx=20,sticky = W)
Label(add_emp_page,text="BRANCH_ID ",font ="none 15",bg ="#fdb9b9")     .grid(row=2,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text = "NAME ",font ="none 15",bg ="#fdb9b9")        .grid(row=3,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text = "Address: Street",font ="none 15",bg ="#fdb9b9") .grid(row=4,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text="Address: State",font ="none 15",bg ="#fdb9b9")    .grid(row=5,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text = "Address: City",font ="none 15",bg ="#fdb9b9")   .grid(row=6,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text = "Address: pin",font ="none 15",bg ="#fdb9b9")    .grid(row=7,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text = "EMAIL ",font ="none 15",bg ="#fdb9b9")      .grid(row=8,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text="GENDER ",font ="none 15",bg ="#fdb9b9")       .grid(row=9,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text = "CONTACT ",font ="none 15",bg ="#fdb9b9")    .grid(row=10,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text="NATIONALITY ",font ="none 15",bg ="#fdb9b9")  .grid(row=11,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text = "DOB",font ="none 15",bg ="#fdb9b9")         .grid(row=12,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text="USERNAME ",font ="none 15",bg ="#fdb9b9")     .grid(row=13,column=0,pady=10,padx=20,sticky = W)
Label(add_emp_page,text="PASSWORD ",font ="none 15",bg ="#fdb9b9")     .grid(row=14,column=0,pady=10,padx=20,sticky = W)
#entry
branch_id_e=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
name_e=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
street_box=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
state_box=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
city_box=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
pin_box=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
email_e=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
gender_e=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
contact_e=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
nationality_e=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
dob_e=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
username_e=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
password_e=Entry(add_emp_page,font ="none 15",bg ="#fdb9b9")
#entry.grid()
branch_id_e     .grid(row=2,column=1,pady=10,padx=20,sticky = W)
name_e          .grid(row=3,column=1,pady=10,padx=20,sticky = W)
street_box.     grid(row=4,column=1,pady=10,padx=20,sticky = W)
state_box.      grid(row=5,column=1,pady=10,padx=20,sticky = W)
city_box.       grid(row=6,column=1,pady=10,padx=20,sticky = W)
pin_box.        grid(row=7,column=1,pady=10,padx=20,sticky = W)
email_e         .grid(row=8,column=1,pady=10,padx=20,sticky = W)
gender_e        .grid(row=9,column=1,pady=10,padx=20,sticky = W)
contact_e       .grid(row=10,column=1,pady=10,padx=20,sticky = W)
nationality_e   .grid(row=11,column=1,pady=10,padx=20,sticky = W)
dob_e           .grid(row=12,column=1,pady=10,padx=20,sticky = W)
username_e      .grid(row=13,column=1,pady=10,padx=20,sticky = W)
password_e      .grid(row=14,column=1,pady=10,padx=20,sticky = W)
#Only Buttons()
register=Button(add_emp_page,text="Register Employee",padx=30,pady=5,command=register_button)
go_back=Button(add_emp_page,text="Go Back",padx=30,pady=5,command=go_back_button)
#button.grid()
register.grid(row=15,column=1,pady=10,padx=20,sticky = W)
go_back.grid(row=16,column=1,pady=10,padx=20,sticky = W)

mainloop()
data_base.commit()
data_base.close()