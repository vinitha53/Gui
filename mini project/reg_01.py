from tkinter import *
from db_02 import *
from PIL import Image, ImageTk
root=Tk()
root.geometry("800x600+300+60")
root.config(bg="light blue")
root.title("image display")
# image=PhotoImage(file="C:/Users/god/Desktop/cc.jpg")
pil_image = Image.open("C:/Users/god/Desktop/image1.jfif")
img = ImageTk.PhotoImage(pil_image)
label1=Label(root,image=img)
label1.grid(row=0,column=2)
db = mydbclass()
def passvalue():
    """Insert new record using the input values."""
    value1 = tbInputValue1.get()
    value2 = tbInputValue2.get()
    value3 = tbInputValue3.get()
    value4 = tbInputValue4.get()
    value5 = tbInputValue5.get()
    value6 = tbInputValue6.get()
    txt = f"v1: {value1}, v2: {value2}, v3: {value3}, v4: {value4}, v5: {value5}, v6: {value6}"
    # lblresultmsg.config(text=txt)

    db.insertvalues(value1, value2,value3,value4,value5,value6)

lblTitle=Label(root,text="register page",bg="pink")
lblTitle.grid(row=1, column=2,padx=10, pady=10)
lblvalue1msg=Label(root,text="Name:", bg="lightblue")
lblvalue1msg.grid(row=3, column=1,padx=10, pady=10)
lblvalue2msg=Label(root,text="Age :", bg="lightblue")
lblvalue2msg.grid(row=4, column=1, padx=10, pady=10)
lblvalue2msg=Label(root,text="Gender :", bg="lightblue")
lblvalue2msg.grid(row=5, column=1, padx=10, pady=10)
lblvalue2msg=Label(root,text="Course :", bg="lightblue")
lblvalue2msg.grid(row=6, column=1, padx=10, pady=10)
lblvalue2msg=Label(root,text="Phone number :", bg="lightblue")
lblvalue2msg.grid(row=7, column=1, padx=10, pady=10)
lblvalue2msg=Label(root,text="Email id :", bg="lightblue")
lblvalue2msg.grid(row=8, column=1, padx=10, pady=10)


tbInputValue1=Entry(root)
tbInputValue1.grid(row=3, column=2, padx=10, pady=20)

tbInputValue2=Entry(root)
tbInputValue2.grid(row=4, column=2, padx=10, pady=20)

tbInputValue3=Entry(root)
tbInputValue3.grid(row=5, column=2, padx=10, pady=20)
tbInputValue4=Entry(root)
tbInputValue4.grid(row=6, column=2, padx=10, pady=20)
tbInputValue5=Entry(root)
tbInputValue5.grid(row=7, column=2, padx=10, pady=20)
tbInputValue6=Entry(root)
tbInputValue6.grid(row=8, column=2, padx=10, pady=20)
btninsert=Button(root,text="Submit",bg="pink",command= passvalue)
btninsert.grid(row=9, column=2, padx=10, pady=20)
lblresultmsg = Label(root, text="")
lblresultmsg.grid(row=9, column=3, padx=10, pady=30)



root.mainloop()