
import sqlite3 as base
# create or connect a data base
data_base = base.connect("demo1.db")
# create a cursor
cursor = data_base.cursor()



cursor.execute("delete FROM transactions ")
print(cursor.fetchall())

x = cursor.fetchall()
print(x)

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


data_base.commit()
data_base.close()