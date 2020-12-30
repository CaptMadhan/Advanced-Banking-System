from tkinter import *
import os
import sqlite3 as base
import datetime
# create or connect a data base
data_base = base.connect("demo1.db")
# create a cursor
cursor = data_base.cursor()

def manager_view():
    admin_page =Tk()
    admin_page.title("KM bank")
    admin_page.configure(bg="#fdb9b9")
    admin_page.iconbitmap("dbmsicon.ico")

    #functions
    def employee_details_f():
        return
    def account_details_f():
        return
    def account_activity_details_f():
        account_activity_details_tk = Toplevel()
        account_activity_details_tk.title("KM bank")
        account_activity_details_tk.configure(bg="#fdb9b9")
        account_activity_details_tk.iconbitmap("dbmsicon.ico")


        Label(account_activity_details_tk,text = "Enter account no.",font ="none 25",bg ="#fdb9b9").grid(row=0,column=0,pady=10,padx=20)
        acc_no_input_activity =Entry(account_activity_details_tk,font ="none 20",bg ="#fdb9b9")
        acc_no_input_activity.grid(row=1,column=0,pady=10,padx=20)
        def get_ac_no():
            ac_no=int(acc_no_input_activity.get())
            get_acc_button.destroy()
            acc_no_input_activity.destroy()
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
            Label(account_activity_details_tk,text ="\tACCOUNT NO\tTRANS ID   \tACTIVITY \tACTIVITY DATETIME\t",font ="none 15",bg ="#fdb9b9", borderwidth=2, relief="ridge",pady=10,padx=10).grid(row=0,column=0,pady=10,padx=10)
            for i in range(len(result)):
                Label(account_activity_details_tk,text = result[i] +"\t",font ="none 15",bg ="#fdb9b9", borderwidth=2, relief="ridge").grid(row=i+1,column=0,pady=10,padx=10)
            def close_button_f():
                account_activity_details_tk.destroy()
            close_button=Button(account_activity_details_tk,text="Close",padx=20,pady=5,height = 2, width = 20,command=close_button_f)
            close_button.grid(row=30,column=0,pady=10,padx=20)
            account_activity_details_tk.grab_set()

        get_acc_button=Button(account_activity_details_tk,text="submit",padx=20,pady=5,height = 2, width = 20,command=get_ac_no)
        get_acc_button.grid(row=2,column=0,pady=10,padx=20)



    def add_employee_f():
        return
    def set_interest_rate_f():
        return
    def add_interest_to_accounts_f():
        return
    def log_out_f():
        admin_page.destroy()
    #Labels
    welcome_message=Label(admin_page,text = "Welcome Manager",font ="Algerian 25",bg ="#fdb9b9")
    #Button
    employee_details=Button(admin_page,text="Employee Details",padx=30,pady=5,height = 2, width = 20,command=employee_details_f)
    account_details=Button(admin_page,text="Account Details",padx=30,pady=5,height = 2, width = 20,command=account_details_f)
    account_activity_details=Button(admin_page,text="Account activity Details",padx=30,pady=5,height = 2, width = 20,command=account_activity_details_f)
    add_employee=Button(admin_page,text="Add Employee",padx=30,pady=5,height = 2, width = 20,command=add_employee_f)
    set_interest_rate=Button(admin_page,text="Set Interest Rate",padx=30,pady=5,height = 2, width = 20,command=set_interest_rate_f)
    add_interest_to_accounts=Button(admin_page,text="Add interest amount to accounts",padx=30,pady=5,height = 2, width = 20,command=add_interest_to_accounts_f)
    log_out_button=Button(admin_page,text="LogOut",padx=30,pady=5,height = 2, width = 20,command=log_out_f)

    #Label.grid()
    welcome_message .grid(row=0,column=0,pady=10,padx=20)
    #Buttone.grid()
    employee_details        .grid(row=1,column=0,pady=10,padx=20)
    add_employee            .grid(row=1,column=1,pady=10,padx=20)
    account_details         .grid(row=2,column=0,pady=10,padx=20)
    account_activity_details.grid(row=2,column=1,pady=10,padx=20)
    set_interest_rate       .grid(row=3,column=0,pady=10,padx=20)
    add_interest_to_accounts.grid(row=3,column=1,pady=10,padx=20)
    log_out_button          .grid(row=4,column=0,pady=10,padx=20)

manager_view()
mainloop()