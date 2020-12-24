import sqlite3 as base
db = base.connect("demo1.db")

cursor = db.cursor()
#cursor.execute(" CREATE TABLE BOOKS(BOOKID INT PRIMARY KEY, BOOK_NAME VARCHAR(50));")
#cursor.execute("INSERT INTO books VALUES(:BOOKID,:BOOK_NAME)",
#                {
#                    'BOOKID': 1004,'BOOK_NAME':"R"
#                }
#                )
cursor.execute("SELECT * FROM books")
print(cursor.fetchall())

db.commit()
db.close()