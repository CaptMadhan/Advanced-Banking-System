from tkinter import *
import sqlite3 as base
# create or connect a data base
data_base = base.connect("demo1.db")
# create a cursor
cursor = data_base.cursor()



cursor.execute("select * from customer")
print(cursor.fetchall())
cursor.execute("select * from account")
print(cursor.fetchall())

data_base.close()