import os 
import mysql.connector




class mydbclass:    
    def MyDBConnection(self):
        dbcon=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Welcome@1",
        database="v"
        )
        return dbcon
    # dbcon=MyDBConnection()
    # print("connected",dbcon)
    def insertvalues(self,v1,v2,v3,v4,v5,v6):
        # value1=tbInputValue1.get()
        # value2=tbInputValue2.get()
        # value3=tbInputValue3.get()
        # value4=tbInputValue4.get()
        # value5=tbInputValue5.get()
        # value6=tbInputValue6.get()
        connection=self.MyDBConnection()
        result=connection.cursor()
        query="INSERT INTO reg01(name,age,gender,course,phoneno,emailid) VALUES (%s,%s,%s,%s,%s,%s);"
    
        valuepass=(v1,v2,v3,v4,v5,v6)
        print(query,valuepass)
        result.execute(query,valuepass)
        connection.commit()
        connection.close()



# dbcon1=MyDBConnection()
# print("connected",dbcon1)
 