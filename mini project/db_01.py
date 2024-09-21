import os 
from tkinter import *
import mysql.connector

app=Tk()

app.title("Student Mark Entry")
app.geometry("800x600+300+60")

def MyDBConnection():
    dbcon=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Welcome@1",
    database="v"
    )
    return dbcon


# dbcon1=MyDBConnection()
# print("connected",dbcon1)
 
def insertvalues():
    value1=tbInputValue1.get()
    value2=tbInputValue2.get()
    connection=MyDBConnection()
    result=connection.cursor()
    query="INSERT INTO value01(value1,value2) VALUES (%s,%s);"
    
    valuepass=(value1,value2)
    print(query,valuepass)
    result.execute(query,valuepass)
    connection.commit()
    connection.close()

def delete():
    sno_get=tbInputValue3.get()
    connection=MyDBConnection()
    result=connection.cursor()
    query="delete from value01 where id="+str(sno_get)+";"
    print(query)
    # query="delete from value01 where id=;"
    # print(query,valuepass1)
    # valuepass1=(sno_get,)
    result.execute(query)
    # result.execute(query,sno_get)
    connection.commit()
    connection.close()


def deletevalues():
    value1=tbInputValue1.get()
    value2=tbInputValue2.get()
    connection=MyDBConnection()
    result=connection.cursor()
    query="delete from value01 where value1=%s and value2=%s;"
    valuepass=(value1,value2)
    result.execute(query,valuepass)
    connection.commit()
    connection.close()
def updatevalues():
    value1=tbInputValue1.get()
    value2=tbInputValue2.get()
    connection=MyDBConnection()
    result=connection.cursor()
    query="update  value01   set value1=%s where value2=%s;"
    valuepass=(value1,value2)
    result.execute(query,valuepass)
    connection.commit()
    connection.close()
def clear_fields():
    
    tbInputValue1.delete(0, END)
    tbInputValue2.delete(0, END)
    lblresultmsg.config(text="Fields cleared")

lblTitle=Label(app,text="student mark Entry",bg="pink")
lblTitle.grid(row=0,padx=40,pady=40)
lblvalue1msg=Label(app,text="Enter Value A :", bg="lightblue")
lblvalue1msg.grid(row=1, column=1, padx=10, pady=30)

lblvalue2msg=Label(app,text="Enter Value B :", bg="lightblue")
lblvalue2msg.grid(row=2, column=1, padx=10, pady=30)

tbInputValue1=Entry(app)
tbInputValue1.grid(row=1, column=2, padx=10, pady=30)

tbInputValue2=Entry(app)
tbInputValue2.grid(row=2, column=2, padx=10, pady=30)

tbInputValue3=Entry(app)
tbInputValue3.grid(row=2, column=3, padx=10, pady=30)

btninsert=Button(app,text="Insert",bg="pink", command=insertvalues)
btninsert.grid(row=3, column=1, padx=10, pady=30)

btnupdate=Button(app,text="Update",bg="pink",command=updatevalues)
btnupdate.grid(row=3, column=2, padx=10, pady=30)

btndelete=Button(app,text="Delete",bg="pink",command=deletevalues)
btndelete.grid(row=3, column=3, padx=10, pady=30)

btndelete1=Button(app,text="Delete by sno",bg="pink",command=delete)
btndelete1.grid(row=3, column=4, padx=10, pady=30)


btnreset=Button(app,text="Reset",command=clear_fields)
btnreset.grid(row=3, column=5, padx=10, pady=30)
lblresultmsg = Label(app, text="")
lblresultmsg.grid(row=4, column=2, padx=10, pady=30)

app.mainloop()