from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dbms_project"
)
mycursor = mydb.cursor()
mycursor.execute("create table if not exists vacc_data(Aadhar_ID varchar(20) primary key, First_Name varchar(20) not null, Last_Name varchar(20) not null, Phone_Number bigint not null, City varchar(50), State varchar(50),Age int)");
root = Tk()
root.title("Vaccination Data")
root.geometry("900x300")
# photo = PhotoImage(file='image.png')
# label12 = Label(root, image=photo).grid(row=8, column=5)
label1 = Label(root, text="Aadhar_Id", width=20, height=2,
               bg="peach puff").grid(row=0, column=0)
label2 = Label(root, text="First_Name", width=20,
               height=2, bg="peach puff").grid(row=1, column=0)
label3 = Label(root, text="Last_Name", width=20,
               height=2, bg="peach puff").grid(row=2, column=0)
label4 = Label(root, text="Phone_Number", width=20,
               height=2, bg="peach puff").grid(row=3, column=0)
label5 = Label(root, text="City", width=20, height=2,
               bg="peach puff").grid(row=4, column=0)
label6 = Label(root, text="State", width=20, height=2,
               bg="peach puff").grid(row=5, column=0)
label7 = Label(root, text="Age", width=20, height=2,
               bg="peach puff").grid(row=6, column=0)
label8 = Label(root, width=10, height=2).grid(row=7, column=2)
label9 = Label(root, width=10, height=2).grid(row=7, column=4)
label10 = Label(root, width=10, height=2).grid(row=7, column=6)
label11 = Label(root, width=10, height=2).grid(row=7, column=8)
e1 = Entry(root, width=30, borderwidth=8)
e1.grid(row=0, column=1)
e2 = Entry(root, width=30, borderwidth=8)
e2.grid(row=1, column=1)
e3 = Entry(root, width=30, borderwidth=8)
e3.grid(row=2, column=1)
e4 = Entry(root, width=30, borderwidth=8)
e4.grid(row=3, column=1)
e5 = Entry(root, width=30, borderwidth=8)
e5.grid(row=4, column=1)
e6 = Entry(root, width=30, borderwidth=8)
e6.grid(row=5, column=1)
e7 = Entry(root, width=30, borderwidth=8)
e7.grid(row=6, column=1)


def Register():
    Aadhar_Id = e1.get()
    dbAadhar_Id = ""
    Select = "select count(*) from vacc_data where Aadhar_Id='%s'" % (Aadhar_Id)
    mycursor.execute(Select)
    result = mycursor.fetchall()
    for i in result:
        dbAadhar_Id = i[0]
    if(int(Aadhar_Id) != int(dbAadhar_Id)):
        Insert = "Insert into vacc_data(Aadhar_Id,First_Name,Last_Name,Phone_Number,City,State,Age) values(%s,%s,%s,%s,%s,%s,%s)"
        First_Name = e2.get()
        Last_Name = e3.get()
        Phone_Number = e4.get()
        City = e5.get()
        State = e6.get()
        Age = e7.get()
        if(First_Name != "" and Last_Name != "" and Phone_Number != "" and City != "" and State != "" and Age != ""):
            Value = (Aadhar_Id, First_Name, Last_Name,
                     Phone_Number, City, State, Age)
            mycursor.execute(Insert, Value)
            mydb.commit()
            messagebox.askokcancel("Information", "Record inserted")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
        else:
            if (First_Name == "" and Last_Name == "" and Phone_Number == "" and City == "" and State == "" and Age == ""):
                messagebox.askokcancel(
                    "Information", "New Entery Fill All Details")
            else:
                messagebox.askokcancel("Error", "Some fields left blank")
    else:
        messagebox.askokcancel("Error", "Record Already exists")




def Delete():
    Aadhar_Id = e1.get()
    Delete = "delete from vacc_data where Aadhar_Id='%s'" % (Aadhar_Id)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information", "Record Deleted")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)


def Update():
    Aadhar_Id = e1.get()
    First_Name = e2.get()
    Last_Name = e3.get()
    Phone_Number = e4.get()
    City = e5.get()
    State = e6.get()
    Age = e7.get()
    Update = "Update vacc_data set First_Name='%s', Last_Name='%s', Phone_Number='%s', City='%s', State='%s', Age='%s' where Aadhar_Id='%s'" % (
        First_Name, Last_Name, Phone_Number, City, State, Age, Aadhar_Id)
    mycursor.execute(Update)
    mydb.commit()
    messagebox.showinfo("Info", "Record Update")


def Showall():
    class A(Frame):
        def _init_(self, parent):
            Frame._init_(self, parent)
            self.CreateUI()
            self.LoadTable()
            self.grid(sticky=(N, S, W, E))
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_columnconfigure(0, weight=1)

        def CreateUI(self):
            tv = Treeview(self)
            tv['columns'] = ('Aadhar_Id', 'First_Name', 'Last_Name',
                             'Phone_Number', 'City', 'State', 'Age')
            tv.heading('#0', text='Aadhar_Id', anchor='center')
            tv.column('#0', anchor='center')
            tv.heading('#1', text='First_Name', anchor='center')
            tv.column('#1', anchor='center')
            tv.heading('#2', text='Last_Name', anchor='center')
            tv.column('#2', anchor='center')
            tv.heading('#3', text='Phone_Number', anchor='center')
            tv.column('#3', anchor='center')
            tv.heading('#4', text='City', anchor='center')
            tv.column('#4', anchor='center')
            tv.heading('#5', text='State', anchor='center')
            tv.column('#5', anchor='center')
            tv.heading('#6', text='Age', anchor='center')
            tv.column('#6', anchor='center')
            tv.grid(sticky=(N, S, W, E))
            self.treeview = tv
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

        def LoadTable(self):
            Select = "Select * from vacc_data"
            mycursor.execute(Select)
            result = mycursor.fetchall()
            Aadhar_Id = ""
            First_Name = ""
            Last_Name = ""
            Phone_Number = ""
            City = ""
            State = ""
            Age = ""
            for i in result:
                Aadhar_Id = i[0]
                First_Name = i[1]
                Last_Name = i[2]
                Phone_Number = i[3]
                City = i[4]
                State = i[5]
                Age = i[6]
                self.treeview.insert("", 'end', text=Aadhar_Id, values=(
                    First_Name, Last_Name, Phone_Number, City, State, Age))
    root = Tk()
    root.title("Overview Page")
    A(root)


def Clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)


button1 = Button(root, text="Register", width=10, height=2,
                 command=Register).grid(row=7, column=0)
button2 = Button(root, text="Delete", width=10, height=2,
                 command=Delete).grid(row=7, column=1)
button3 = Button(root, text="Update", width=10, height=2,
                 command=Update).grid(row=7, column=3)
button5 = Button(root, text="Show Data", width=10, height=2,
                 command=Showall).grid(row=7, column=7)
button6 = Button(root, text="Clear", width=10, height=2,
                 command=Clear).grid(row=7, column=9)
root.mainloop()