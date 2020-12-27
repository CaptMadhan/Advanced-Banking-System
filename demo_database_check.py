import sqlite3 as base

# create or connect a data base
data_base = base.connect("demo1.db")

# create a cursor
cursor = data_base.cursor()


cursor.execute(''' create table if not exists customerID_generator(row int primary key ,cust_id_g int)
''')
#cursor.execute("INSERT INTO customerID_generator VALUES (:row, :cust_id_g)",
#              {
#                 'row':1 ,
#                'cust_id_g':110011000
#           }
#
#              )

cursor.execute("SELECT cust_id_g FROM customerID_generator where row =1")
x = cursor.fetchall()
cust_id_ =x[0][0]+1
print(cust_id_)
cursor.execute("UPDATE customerID_generator SET cust_id_g = :cust_id_d WHERE row=1;",{
    'cust_id_d':x[0][0]+1
    }
    )
cursor.execute('''create table IF NOT EXISTS CUSTOMER(
CUST_ID INT PRIMARY KEY,
PASSWORD VARCHAR(20),
NAME VARCHAR(50),
DOB DATE,
AGE INT,
GENDER VARCHAR(6),
EMAIL VARCHAR(50),
CONTACT INT,
PAN INT,
NATIONALITY VARCHAR(15)
);''')
cursor.execute('''create table IF NOT EXISTS CUSTOMER_Address(
CUST_ID INT PRIMARY KEY,
STREET VARCHAR(50),
CITY VARCHAR(20),
STATE VARCHAR(20),
PIN INT,
Foreign Key(CUST_ID) REFERENCES CUSTOMER(CUST_ID) ON DELETE CASCADE
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS INTEREST(
INTEREST_ID INT PRIMARY KEY,
SAVING_INT FLOAT
);''')


cursor.execute('''CREATE TABLE IF NOT EXISTS ACCOUNT(
AC_NO INT PRIMARY KEY,
INTEREST_ID INT,
CUST_ID INT,
AC_TYPE VARCHAR(10),
BALANCE INT, 
INTEREST_AMOUNT INT,
INTEREST_RATE INT,
OPEN_DATE DATE,
Foreign Key(CUST_ID) REFERENCES CUSTOMER(CUST_ID) ON DELETE CASCADE,
Foreign Key(INTEREST_ID) REFERENCES INTEREST(INTEREST_ID) ON DELETE CASCADE
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS BRANCH(
BRANCH_ID INT PRIMARY KEY,
BRANCH_NAME VARCHAR(50)
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS BRANCH_ADDRESS(
BRANCH_ID INT PRIMARY KEY,
STATE VARCHAR(20),
COUNTRY VARCHAR(20),
PIN INT,
Foreign Key(BRANCH_ID) REFERENCES BRANCH(BRANCH_ID) ON DELETE CASCADE
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS OFFICER(
EMP_ID INT PRIMARY KEY,
BRANCH_ID INT,
NAME VARCHAR(50),
EMAIL VARCHAR(50),
GENDER VARCHAR(6),
CONTACT INT,
NATIONALITY VARCHAR(20),
DOB DATE,
USERNAME VARCHAR(20),
PASSWORD VARCHAR(20),
Foreign Key(BRANCH_ID) REFERENCES BRANCH(BRANCH_ID) ON DELETE CASCADE
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS OFFICER_ADDRESS(
EMP_ID INT PRIMARY KEY,
STREET VARCHAR(50),
CITY VARCHAR(50),
STATE VARCHAR(50),
PIN INT,
Foreign Key(EMP_ID) REFERENCES OFFICER(EMP_ID) ON DELETE CASCADE
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS MANAGER(
EMP_ID INT PRIMARY KEY,
BRANCH_ID INT ,
NAME VARCHAR(50),
EMAIL VARCHAR(50),
GENDER VARCHAR(6),
CONTACT INT,
NATIONALITY VARCHAR(20),
DOB DATE,
USERNAME VARCHAR(20),
PASSWORD VARCHAR(20),
Foreign Key(BRANCH_ID) REFERENCES BRANCH(BRANCH_ID) ON DELETE CASCADE
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS MANAGER_ADDRESS(
EMP_ID INT PRIMARY KEY,
STREET VARCHAR(50),
CITY VARCHAR(50),
STATE VARCHAR(50),
PIN INT,
Foreign Key(EMP_ID) REFERENCES OFFICER(EMP_ID) ON DELETE CASCADE
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS TRANSACTIONS(
AC_NO INT ,
TRANS_ID INT PRIMARY KEY,
TRANS_TYPE VARCHAR(20),
DATE_OF_TRANS DATE,
Foreign Key(AC_NO) REFERENCES ACCOUNT(AC_NO) ON DELETE CASCADE);
''')

cursor.execute("SELECT * FROM CUSTOMER")
cursor.execute("SELECT * FROM CUSTOMER_Address")
cursor.execute("SELECT * FROM INTEREST")
cursor.execute("SELECT * FROM ACCOUNT")
cursor.execute("SELECT * FROM BRANCH")
cursor.execute("SELECT * FROM OFFICER")
cursor.execute("SELECT * FROM BRANCH_ADDRESS")
cursor.execute("SELECT * FROM OFFICER_ADDRESS")
cursor.execute("SELECT * FROM MANAGER")
cursor.execute("SELECT * FROM MANAGER_ADDRESS")
cursor.execute("SELECT * FROM TRANSACTIONS")

#######################################################################################
#admin login data
'''cursor.execute("INSERT INTO CUSTOMER VALUES (:CUST_ID,:password,:NAME, :DOB, :AGE,:GENDER,:EMAIL,:Contact,:pan,:nationality)",
    {
                   
                   'CUST_ID':11111111,
                   'password':12345678,
                   'NAME': "ADMIN",
                   'DOB':'2000-06-01' ,
                   'AGE':20 ,
                   'GENDER':'Male' ,
                   'EMAIL': 'hahahahaha',
                   'Contact': 1010101010,
                   'pan': 1010212212,
                   'nationality':"Indian" 
    })
cursor.execute("INSERT INTO CUSTOMER_address VALUES (:CUST_ID, :STREET,:CITY,:STATE,:PIN)",
                {
                    'CUST_ID':11111111,
                    'STREET':"llllll",
                    'STATE':"Karnataka",
                    'CITY':"bangalore" ,
                    'PIN':560071
                })
cursor.execute("SELECT * FROM CUSTOMER")
print(cursor.fetchall())
cursor.execute("SELECT * FROM CUSTOMER_ADDRESS")
print(cursor.fetchall())
'''
#######################################################################################
#cursor.execute("DELETE from users WHERE oid='0'")

x =cursor.fetchall()
for i in x:
    print(x)

# commit all the changes
data_base.commit()

# close the database
data_base.close()