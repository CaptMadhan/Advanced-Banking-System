from tkinter import *
import sqlite3 as base
from datetime import date
data_base = base.connect("demo1.db")
cursor = data_base.cursor()

def acct_exec(cust_id_):
    account_page =Tk()
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
    ###########################################################################################################
    #functions

    def chkchk():
        l = Label(account_page, bg='white', width=20, text='empty')
        l.grid(row=2,column=0,pady=10,padx=20,sticky = W)
        if (svg1.get() == 1) & (cur1.get() == 0):
            l.config(text='Savings Account Selected')
        elif (svg1.get() == 0) & (cur1.get() == 1):
            l.config(text='Current Account Selected')
        elif (svg1.get() == 0) & (cur1.get() == 0):
            l.config(text='Select any one')
        else:
            l.config(text='Select any one not both ')    

    balance =       0
    interest_id =   0
    interest_rate = 0
    interest_amt =  0
    def submit_button_f():
        global savings
        global current
        global balance
        global interest_amt
        global interest_id
        global interest_rate
        l = Label(account_page, bg='white', width=20, text='empty')
        l.grid(row=4,column=0,pady=10,padx=20,sticky = W)
        if (svg1.get() == 1) & (cur1.get() == 1):
            l.config(text='Select Only One')
            return
        elif (svg1.get() == 0) & (cur1.get() == 0):
            l.config(text='Select any one')
            return
        else:
            savings = svg1.get()
            current = cur1.get()
            l.config(text='Fixed')
        print(savings)
        print(current)
        if savings == 1 and current ==0:
            interest_id = 1
            interest_rate = 10
            interest_amt = 0
            balance = 0
        else:
            interest_id = 0
            interest_rate = 0
            interest_amt = 0
            balance = 0
        
        if savings == 1:
            acc_type ="Savings"
        elif current ==1:
            acc_type ="Current"
        Open_date = date.today()
        print(savings)
        print(current)
        print(balance)
        print(interest_amt)
        print(interest_id)
        print(acc_type)
        print(interest_rate)
        print(Open_date)
        cursor.execute("INSERT INTO ACCOUNT VALUES (:AC_NO,:INTEREST_ID,:CUST_ID,:AC_TYPE,:BALANCE,:INTEREST_AMOUNT,:INTEREST_RATE,:OPEN_DATE)",
        {
            
            'AC_NO':acc_no,
            'INTEREST_ID':interest_id,
            'CUST_ID': cust_id_,
            'AC_TYPE':acc_type ,
            'BALANCE':balance ,
            'INTEREST_AMOUNT':interest_amt ,
            'INTEREST_RATE': interest_rate,
            'OPEN_DATE':Open_date 
            })
        account_page.destroy()

    #Account Labels
    acc_no_l=Label(account_page,text = "Account No.",font ="none 15",bg ="#fdb9b9")
    acc_no_d=Label(account_page,text = acc_no,font ="none 15",bg ="#fdb9b9")
    #Checkbuttons
    svg1 = IntVar()
    cur1 = IntVar()
    savings = 0
    current = 0
    svg_chk =   Checkbutton(account_page, text='Saving',variable=svg1, onvalue=1, offvalue=0,command=chkchk)
    cur_chk=    Checkbutton(account_page, text='Current',variable=cur1, onvalue=1, offvalue=0,command=chkchk)

    #################################################################################################33
    #buttons
    submit_button_account=Button(account_page,text="Submit",padx=30,pady=5,command=submit_button_f)
    #Label.grid()
    acc_no_l.    grid(row=1,column=0,pady=10,padx=20,sticky = W)
    acc_no_d.    grid(row=1,column=1,pady=10,padx=20,sticky = W)
    svg_chk.     grid(row=2,column=1,pady=10,padx=20,sticky = W)
    cur_chk.     grid(row=3,column=1,pady=10,padx=20,sticky = W)

    #Button.grid()
    submit_button_account.     grid(row=4,column=1,pady=10,padx=20,sticky = W)

    
    ##################################################################################################3
    mainloop()
    data_base.commit()  
#acct_exec(1001110011)
data_base.close()