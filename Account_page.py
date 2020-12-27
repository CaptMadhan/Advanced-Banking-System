from tkinter import *
import sqlite3 as base
data_base = base.connect("demo1.db")
cursor = data_base.cursor()

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


mainloop()
data_base.commit()
data_base.close()