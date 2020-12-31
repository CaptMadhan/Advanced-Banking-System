from tkinter import *
import sqlite3 as base
# create or connect a data base
data_base = base.connect("demo1.db")
# create a cursor
cursor = data_base.cursor()
def set_interest_rate_f():
    set_interest_rate = Tk()
    set_interest_rate.title("KM bank")
    set_interest_rate.configure(bg="#fdb9b9")
    set_interest_rate.iconbitmap("dbmsicon.ico")

    cursor.execute("SELECT SAVING_INT  FROM INTEREST where INTEREST_ID  =1")
    x= cursor.fetchall()
    current_int_amt=x[0][0]
    Label(set_interest_rate,text ="Current Interest Rate for savings account" ,font ="none 25",bg ="#fdb9b9").grid(row=0,column=0,pady=10,padx=20)
    Label(set_interest_rate,text =current_int_amt ,font ="none 25",bg ="#fdb9b9").grid(row=1,column=0,pady=10,padx=20)
    Label(set_interest_rate,text ="Enter new Interest Rate" ,font ="none 25",bg ="#fdb9b9").grid(row=2,column=0,pady=10,padx=20)
    new_interest_rate_e =Entry(set_interest_rate,font ="none 20",bg ="#fdb9b9")
    new_interest_rate_e.grid(row=3,column=0,pady=10,padx=20)

    def set_new_int_rate():
        new_interest_rate = new_interest_rate_e.get()
        if new_interest_rate =='':
            Label(set_interest_rate,text ="Enter any value or close",font ="none 15",bg ="#fdb9b9").grid(row=31,column=0,pady=10,padx=20)
            return
        cursor.execute("UPDATE INTEREST SET SAVING_INT  = :SAVING_INT  WHERE INTEREST_ID =1;",{
        'SAVING_INT':new_interest_rate
        }
        ) 
        submit_int_rate.destroy()
        Label(set_interest_rate,text ="Interest rate set to "+ str(new_interest_rate) ,font ="none 25",bg ="#fdb9b9").grid(row=4,column=0,pady=10,padx=20)

    submit_int_rate=Button(set_interest_rate,text="submit",padx=20,pady=5,height = 2, width = 20,command=set_new_int_rate)
    submit_int_rate.grid(row=4,column=0,pady=10,padx=20)
    def close_button_f():
        set_interest_rate.destroy()
    close_button=Button(set_interest_rate,text="Close",padx=20,pady=5,height = 2, width = 20,command=close_button_f)
    close_button.grid(row=30,column=0,pady=10,padx=20)
    set_interest_rate.grab_set()

set_interest_rate_f()
mainloop()