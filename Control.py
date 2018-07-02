from tkinter import  *
from tkinter import ttk
from tkinter import messagebox

from DBConnect_class import DBConnect
from ListReservation import ListTickets
dbconnect=DBConnect()


root = Tk()
ttk.Label(root,text="Full name:").grid(row=0,column=0,pady=10,padx=10)
EntryFullname=ttk.Entry(root,width=30,font=('Arial',16))
EntryFullname.grid(row=0,column=1,columnspan=2)
root.title("Ticket Reservation")
#style
root.configure(background="#e1d8b2")
style=ttk.Style()
style.theme_use("classic")
style.configure("TLabel",background="#e1d8b2")
style.configure("TButton",background="#e1d8b2")
style.configure("TRadiobutton",background="#e1d8b2")
SpanGender=StringVar()
SpanGender.set("Male")
ttk.Label(root,text="Gender").grid(row=1,column=0)
ttk.Radiobutton(root,text="Male",variable=SpanGender, value="Male").grid(row=1,column=1)
ttk.Radiobutton(root,text="Female",variable=SpanGender, value="Female").grid(row=1,column=2)


TextComments=Text(root,width=30,height= 15,font= ('Arial',16))
TextComments.grid(row=3,column=1,columnspan=2)

ttk.Label(root,text="Comments:").grid(row=3,column=0)

BuButton=ttk.Button(root,text="Submit")
BuButton.grid(row=4,column=3)

BuList=ttk.Button(root,text="List")
BuList.grid(row=4,column=2)


BuDelete=ttk.Button(root,text="Delete")
BuDelete.grid(row=5,column=3)


BuUpdate=ttk.Button(root,text="Update")
BuUpdate.grid(row=5,column=2)



def ButtonClick():
    print("Full Name: {}". format(EntryFullname.get()))
    print("Gender: {}".format(SpanGender.get()))
    print("Comments: {}".format(TextComments.get(1.0,'end')))
    msg=dbconnect.Add(EntryFullname.get(),SpanGender.get(), TextComments.get(1.0, 'end'))
    messagebox.showinfo(title="ADD info",message=msg)
    EntryFullname.delete(0,'end')
    TextComments.delete(1.0,'end')

def ButtonList():
    listTickets=ListTickets()

def ButtonDelete():
    print("enter ID to be deleted :{}")

def ButtonUpdate():
    print("b")


BuButton.config(command=ButtonClick)

BuList.config(command=ButtonList)

BuDelete.config(command=ButtonDelete)

BuUpdate.config(command=ButtonUpdate)

root.mainloop()

