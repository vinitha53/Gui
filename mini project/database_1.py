import os
from tkinter import *
import mysql.connector

app=Tk()

app.title("Student Mark Entry")
app.geometry("800x600+300+60")



def MyDBConnection():
      
        dbcon = mysql.connector.connect(                                                    
            host="127.0.0.1",
            user="root",
            password="Welcome@1",
            database="v"
        )
     
    #   return dbcon
# print("connected to database at",dbcon)        

dbcon1=MyDBConnection()
print(dbcon1) 


# def insertrecord():
       
#         cursor = dbcon1.cursor()
#         statement = "INSERT INTO record (value1, value2) VALUES (23, 23);"
#         cursor.execute(statement)
#         dbcon1.commit()
#         dbcon1.close()


lblTitle=Label(app,text="Student Mark Entry", bg="red", fg="white")
lblTitle.grid(row=0, padx=50, pady=30)


lblvalue1msg=Label(app,text="Enter Value A :", bg="black", fg="white")
lblvalue1msg.grid(row=1, column=1, padx=10, pady=30)

lblvalue2msg=Label(app,text="Enter Value B :", bg="black", fg="white")
lblvalue2msg.grid(row=2, column=1, padx=10, pady=30)

tbInputValue1=Entry(app)
tbInputValue1.grid(row=1, column=2, padx=10, pady=30)

tbInputValue2=Entry(app)
tbInputValue2.grid(row=2, column=2, padx=10, pady=30)

btninsert=Button(app,text="Insert")
btninsert.grid(row=3, column=1, padx=10, pady=30)

btnupdate=Button(app,text="Update")
btnupdate.grid(row=3, column=2, padx=10, pady=30)

btndelete=Button(app,text="Delete")
btndelete.grid(row=3, column=3, padx=10, pady=30)

btnreset=Button(app,text="Reset")
btnreset.grid(row=3, column=4, padx=10, pady=30)

lblresultmsg = Label(app, text="not yet connected", bg="black", fg="white", wraplength=500)
lblresultmsg.grid(row=4, column=2, padx=10, pady=30)



app.mainloop()