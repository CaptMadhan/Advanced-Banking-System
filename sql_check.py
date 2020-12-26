import sqlite3 as base

# create or connect a data base
data_base = base.connect("demo1.db")

# create a cursor
cursor = data_base.cursor()
cursor.execute("SELECT * from customer;")
x =cursor.fetchall()
print(x)

    

data_base.close()
