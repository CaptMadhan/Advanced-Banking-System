import sqlite3 as base

# create or connect a data base
data_base = base.connect("demo1.db")

# create a cursor
cursor = data_base.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (book_id int primary key, age int)")
cursor.execute("INSERT INTO users VALUES (:x, :age)",
               {
                   'x': 1004,
                   'age':22
               }

               )

cursor.execute("SELECT *, oid FROM users")


#cursor.execute("DELETE from users WHERE oid='0'")
print(cursor.fetchall())


# commit all the changes
data_base.commit()

# close the database
data_base.close()