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
#cursor.execute("INSERT INTO ACCOUNT VALUES(665566999,1,77777777,'savings',0,0,10,'2020-02-02')")
cursor.execute("select * from deleted_accounts")
print(cursor.fetchall())
data_base.commit()
data_base.close()