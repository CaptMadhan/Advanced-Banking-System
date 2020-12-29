from tkinter import *
import sqlite3 as base
# create or connect a data base
data_base = base.connect("demo1.db")
# create a cursor
cursor = data_base.cursor()

mini_statement =Tk()
mini_statement.title("KM bank")
mini_statement.configure(bg="#fdb9b9")
mini_statement.iconbitmap("dbmsicon.ico")

#cursor.execute("delete from customer ")
#print(cursor.fetchall())
ac_no = 66556655059
cursor.execute("SELECT * FROM transactions where ac_no =:ac_no",{'ac_no':ac_no})
x = cursor.fetchall()
if not len(x):
    Label(mini_statement,text ="No Transactions",font ="none 15",bg ="#fdb9b9", borderwidth=2, relief="ridge").grid(row=0,column=0,pady=10,padx=10)
i=0
j=0
result =[]
var=' '
print("\t ACCOUNT NUMBER\t\tTRANSACTION ID \t\tACTIVITY \t\tACTIVITY DATE")
for i in range(len(x[i])):
    for j in range(len(x[j])):
        var=var+"\t" +str(x[i][j]) 
    result.append(var)
    var=''
    print(result)
i=0
Label(mini_statement,text ="\tACCT NO.\tTRANS ID\t ACTIVITY\t  DATE            ",font ="none 15",bg ="#fdb9b9", borderwidth=2, relief="ridge",pady=10,padx=10).grid(row=0,column=0,pady=10,padx=10)
for i in range(len(result)):
    Label(mini_statement,text = result[i] +"\t",font ="none 15",bg ="#fdb9b9", borderwidth=2, relief="ridge").grid(row=i+1,column=0,pady=10,padx=10)
def close_button_f():
    mini_statement.destroy()
close_button=Button(mini_statement,text="Close",padx=20,pady=5,height = 2, width = 20,command=close_button_f)
close_button.grid(row=i+10,column=0,pady=10,padx=20)
mini_statement.grab_set()
mainloop()







data_base.commit()
data_base.close()