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

#cursor.execute("DELETE FROM ACCOUNT WHERE AC_NO = :AC_NO",{'AC_NO':665566999})
cursor.execute("SELECT * FROM BACKUP_TRANSACTIONS_DATA")
print(cursor.fetchall())

cursor.execute("SELECT * FROM BACKUP_ACCOUNTS_DATA")

print(cursor.fetchall())
data_base.commit()
data_base.close()