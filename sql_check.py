import sqlite3 as base

# create or connect a data base
data_base = base.connect("demo1.db")

# create a cursor
cursor = data_base.cursor()
cursor.execute("SELECT cust_id_g FROM customerID_generator where row =1")
x = cursor.fetchall()
cust_id_ =x[0][0]+1
print(cust_id_)
cursor.execute("UPDATE customerID_generator SET cust_id_g = :cust_id_d WHERE row=1;",{
    'cust_id_d':x[0][0]+1
    }
    )
    

data_base.close()
