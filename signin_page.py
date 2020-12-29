from tkinter import *
import sqlite3 as base
import datetime 
data_base = base.connect("demo1.db")
cursor = data_base.cursor()

def customer_signin_window(cust_id_):
    signin_page =Tk()
    signin_page.title("KM bank")
    signin_page.configure(bg="#fdb9b9")
    signin_page.iconbitmap("dbmsicon.ico")

    def check_balance_f():
        balance_page =Toplevel()
        balance_page.title("KM bank")
        balance_page.configure(bg="#fdb9b9")
        balance_page.iconbitmap("dbmsicon.ico")
        cursor.execute("SELECT BALANCE from account WHERE AC_NO = :ACNO;",{ 'ACNO':ac_no})
        b = cursor.fetchall()
        balance =b[0][0]
        balance_l=Label(balance_page,text = "  Your Current Balance: "+ str(balance)+"  ",font ="none 25",bg ="#fdb9b9")
        balance_l.grid(row=0,column=0,pady=10,padx=20)
        def close_button_f():
            balance_page.destroy()
        close_button=Button(balance_page,text="Close",padx=30,pady=10,height = 2, width = 20,command=close_button_f)
        close_button.grid(row=1,column=0,pady=10,padx=20)
        balance_page.grab_set()

    def deposit_f():
        deposit_page =Toplevel()
        deposit_page.title("KM bank")
        deposit_page.configure(bg="#fdb9b9")
        deposit_page.iconbitmap("dbmsicon.ico")
        deposit_test_l=             Label(deposit_page,text = "  Enter amount to deposit: ",font ="none 25",bg ="#fdb9b9")
        deposit_amount_entry=       Entry(deposit_page,font ="none 25")
        deposit_test_l          .grid(row=0,column=0,pady=10,padx=20)
        deposit_amount_entry    .grid(row=1,column=0,pady=10,padx=20)
        def submit_button_f():
            cursor.execute("SELECT BALANCE from account WHERE AC_NO = :ACNO;",{ 'ACNO':ac_no})
            b = cursor.fetchall()
            balance =b[0][0]
            if deposit_amount_entry.get() == '':
                Label(deposit_page,text = "  Enter amount to deposit or Close ",font ="none 10",bg ="#fdb9b9").grid(row=1,column=1,pady=10,padx=20)
            elif deposit_amount_entry.get().isdigit():
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
                    'TRANS_TYPE': "\tDEPOSITED +"+ str(deposit_amount_entry.get())+"\t",
                    'DATE_OF_TRANS':date_of_trans 
                    })


                updated_balance=balance+int(deposit_amount_entry.get())
                cursor.execute("UPDATE account SET balance = :balance WHERE AC_NO = :ACNO;",{ 'balance':updated_balance,'ACNO':ac_no})
                submit_button.destroy()
                Label(deposit_page,text = "Rs "+str(deposit_amount_entry.get())+" deposited",font ="none 25",bg ="#fdb9b9").grid(row=2,column=0,pady=10,padx=20)
            else:
                Label(deposit_page,text = "  Enter only numbers ",font ="none 10",bg ="#fdb9b9").grid(row=1,column=1,pady=10,padx=20)

            
        submit_button=Button(deposit_page,text="Deposit",padx=30,pady=10,height = 2, width = 20,command=submit_button_f)
        submit_button.grid(row=2,column=0,pady=10,padx=20)
        def close_button_f():
            deposit_page.destroy()
        close_button=Button(deposit_page,text="Close",padx=30,pady=10,height = 2, width = 20,command=close_button_f)
        close_button.grid(row=3,column=0,pady=10,padx=20)
        deposit_page.grab_set()
        
    def withdraw_f():
        withdraw_page =Toplevel()
        withdraw_page.title("KM bank")
        withdraw_page.configure(bg="#fdb9b9")
        withdraw_page.iconbitmap("dbmsicon.ico")
        withdraw_test_l=             Label(withdraw_page,text = "  Enter amount to withdraw: ",font ="none 25",bg ="#fdb9b9")
        withdraw_amount_entry=       Entry(withdraw_page,font ="none 25")
        withdraw_test_l          .grid(row=0,column=0,pady=10,padx=20)
        withdraw_amount_entry    .grid(row=1,column=0,pady=10,padx=20)
        def submit_button_f_w():
            cursor.execute("SELECT BALANCE from account WHERE AC_NO = :ACNO;",{ 'ACNO':ac_no})
            b = cursor.fetchall()
            balance =b[0][0]
            if withdraw_amount_entry.get() == '':
                Label(withdraw_page,text = "  Enter amount to withdraw or Close ",font ="none 10",bg ="#fdb9b9").grid(row=1,column=1,pady=10,padx=20)
            elif withdraw_amount_entry.get().isdigit():
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
                    'TRANS_TYPE': "\tWITHDREW -"+ str(withdraw_amount_entry.get())+"\t",
                    'DATE_OF_TRANS':date_of_trans 
                    })


                updated_balance=balance - int(withdraw_amount_entry.get())
                cursor.execute("UPDATE account SET balance = :balance WHERE AC_NO = :ACNO;",{ 'balance':updated_balance,'ACNO':ac_no})
                submit_button.destroy()
                Label(withdraw_page,text = "Rs "+str(withdraw_amount_entry.get())+" withdrawn",font ="none 25",bg ="#fdb9b9").grid(row=2,column=0,pady=10,padx=20)
            else:
                Label(withdraw_page,text = "  Enter only numbers ",font ="none 10",bg ="#fdb9b9").grid(row=1,column=1,pady=10,padx=20)

            
        submit_button=Button(withdraw_page,text="withdraw",padx=30,pady=10,command=submit_button_f_w)
        submit_button.grid(row=2,column=0,pady=10,padx=20)
        def close_button_f():
            withdraw_page.destroy()
        close_button=Button(withdraw_page,text="Close",padx=30,pady=10,height = 2, width = 20,command=close_button_f)
        close_button.grid(row=3,column=0,pady=10,padx=20)
        withdraw_page.grab_set()


    def mini_statement_f():
        mini_statement =Toplevel()
        mini_statement.title("KM bank")
        mini_statement.configure(bg="#fdb9b9")
        mini_statement.iconbitmap("dbmsicon.ico")
        cursor.execute("SELECT * FROM transactions where ac_no =:ac_no",{'ac_no':ac_no})
        print(ac_no)
        x = cursor.fetchall()
        i=0
        j=0
        result =[]
        var=' '
        for i in range(len(x)):
            for j in range(4):
                var=var+"\t" +str(x[i][j]) 
            result.append(var)
            var=' '
        i=0
        Label(mini_statement,text ="\tACCT NO.\tTRANS ID\t ACTIVITY\t  DATE            ",font ="none 15",bg ="#fdb9b9", borderwidth=2, relief="ridge",pady=10,padx=10).grid(row=0,column=0,pady=10,padx=10)
        for i in range(len(result)):
            Label(mini_statement,text = result[i] +"\t",font ="none 15",bg ="#fdb9b9", borderwidth=2, relief="ridge").grid(row=i+1,column=0,pady=10,padx=10)
        def close_button_f():
            mini_statement.destroy()
        close_button=Button(mini_statement,text="Close",padx=20,pady=5,height = 2, width = 20,command=close_button_f)
        close_button.grid(row=30,column=0,pady=10,padx=20)
        mini_statement.grab_set()


    def log_out_f():
        signin_page.destroy()
    cursor.execute("SELECT AC_NO from account WHERE CUST_ID = :CUSTID;",{ 'CUSTID':cust_id_})
    x = cursor.fetchall()
    ac_no=x[0][0]
    #print(ac_no)
    cursor.execute("SELECT NAME from customer WHERE CUST_ID = :CUSTID;",{ 'CUSTID':cust_id_})
    n = cursor.fetchall()
    name = n[0][0]
    #print(balance)
    #Label
    welcome_message=Label(signin_page,text = "Welcome "+name,font ="Algerian 25",bg ="#fdb9b9")
    #Button
    check_balance=Button(signin_page,text="Check Balance",padx=30,pady=5,height = 2, width = 20,command=check_balance_f)
    deposit=Button(signin_page,text="Deposit",padx=30,pady=5,height = 2, width = 20,command=deposit_f)
    withdraw=Button(signin_page,text="Withdraw",padx=30,pady=5,height = 2, width = 20,command=withdraw_f)
    mini_statement=Button(signin_page,text="Mini Statement",padx=30,pady=5,height = 2, width = 20,command=mini_statement_f)
    log_out_button=Button(signin_page,text="LogOut",padx=30,pady=5,height = 2, width = 20,command=log_out_f)

    #Label.grid()
    welcome_message .grid(row=0,column=0,pady=10,padx=20)
    #Buttone.grid()
    check_balance   .grid(row=1,column=0,pady=10,padx=20)
    deposit         .grid(row=2,column=0,pady=10,padx=20)
    withdraw        .grid(row=1,column=1,pady=10,padx=20)
    mini_statement  .grid(row=2,column=1,pady=10,padx=20)
    log_out_button  .grid(row=3,column=0,pady=10,padx=20)

    


    mainloop()

customer_signin_window(110011062)
data_base.commit()


