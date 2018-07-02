from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DBConnect_class import DBConnect

class ListTickets:
    def __init__(self):
        self._dbConnect=DBConnect()
        self._root=Tk()
        self._root.title("Reserved Ticket List")
        tv=ttk.Treeview(self._root)
        tv.pack()

        tv.heading("#0",text="ID")
        tv.configure(column=('Name','Gender','Comment'))
        tv.heading("Name",text="Full Name")
        tv.heading("Gender",text="Gender")
        tv.heading("Comment",text="Comment")
        cursor=self._dbConnect.ListTickets()
        for row in cursor:
            for row in cursor:
                tv.insert('','end','#{}'.format(row["ID"], row["Name"], row["Gender"],row["Comment"]))
                tv.set('#{}'.format(row["ID"]),'Name',row["Name"])
                tv.set('#{}'.format(row["ID"]), 'Gender', row["Gender"])
                tv.set('#{}'.format(row["ID"]), 'Comment', row["Comment"])

                #print("ID:{}, Name:{},Gender:{},Comment:{}".format(row["ID"], row["Name"], row["Gender"], row["Comment"]))


        self._root.mainloop()