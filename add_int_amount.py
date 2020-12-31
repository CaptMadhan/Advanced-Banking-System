from tkinter import *
import sqlite3 as base
import datetime
# create or connect a data base
data_base = base.connect("demo1.db")
# create a cursor
cursor = data_base.cursor()







def add_interest_to_accounts_f():
    add_int_acc_page = Tk()
    add_int_acc_page.title("KM bank")
    add_int_acc_page.configure(bg="#fdb9b9")
    add_int_acc_page.iconbitmap("dbmsicon.ico")

    def CONFIRM_f():
        cursor.execute("select AC_NO from ACCOUNT")
        x = cursor.fetchall()
        i=0
        for i in range(len(x)):
            ac_no=x[i][0]
            cursor.execute("select BALANCE  from ACCOUNT where AC_NO =:AC_NO",{'AC_NO':ac_no})
            balance_fetch= cursor.fetchall()
            balance = float(balance_fetch[0][0])
            cursor.execute("select INTEREST_RATE from ACCOUNT where AC_NO =:AC_NO",{'AC_NO':ac_no})
            interest_rate_fetch= cursor.fetchall()
            int_rate = float(interest_rate_fetch[0][0]) 
            updated_balance = round((balance + balance*int_rate*0.001),3) 
            cursor.execute("UPDATE account SET balance= :balance;",{
            'balance':updated_balance
            }
            )
            cursor.execute("SELECT trans_id_g FROM transactionID_generator where row =1")
            t = cursor.fetchall()
            trans_id =t[0][0]
            print("TransID = "+ str(trans_id))
            cursor.execute("UPDATE transactionID_generator SET trans_id_g = :trans_id_g WHERE row=1;",
            {
                'trans_id_g':t[0][0]+1
                })
            date_of_trans = datetime.datetime.now()

            cursor.execute("INSERT INTO TRANSACTIONS VALUES (:AC_NO,:TRANS_ID ,:TRANS_TYPE ,:DATE_OF_TRANS )",
            {
                
                'AC_NO':ac_no,
                'TRANS_ID':trans_id,
                'TRANS_TYPE': "\tSavingsINT +"+ str(updated_balance)+"\t",
                'DATE_OF_TRANS':date_of_trans 
                })
        confirm_button.destroy()
        Label(add_int_acc_page,text ="Interest amount added to all accounts" ,font ="none 25",bg ="#fdb9b9").grid(row=1,column=0,pady=10,padx=20)
    Label(add_int_acc_page,text ="Confirm to add interest amount to all accounts" ,font ="none 25",bg ="#fdb9b9").grid(row=0,column=0,pady=10,padx=20)
    confirm_button=Button(add_int_acc_page,text="CONFIRM",padx=20,pady=5,height = 2, width = 20,command=CONFIRM_f)
    confirm_button.grid(row=1,column=0,pady=10,padx=20)
add_interest_to_accounts_f()
data_base.commit()
mainloop()
data_base.close()