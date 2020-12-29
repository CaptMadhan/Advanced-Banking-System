import sqlite3 as base
# create or connect a data base
data_base = base.connect("demo1.db")
# create a cursor
cursor = data_base.cursor()



#cursor.execute("delete from customer ")
#print(cursor.fetchall())
cursor.execute("SELECT * FROM transactions")
print(cursor.fetchall())








data_base.commit()
data_base.close()