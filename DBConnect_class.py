import sqlite3

class DBConnect:

    def __init__(self):
        self._db=sqlite3.connect("Reservation.db")
        self._db.row_factory=sqlite3.Row
        self._db.execute("CREATE TABLE IF NOT EXISTS Ticket(ID integer PRIMARY KEY AUTOINCREMENT,Name text,Gender text,Comment Text)")
        self._db.commit()


    def Add(self,Name,Gender,Comment):
        self._db.row_factory=sqlite3.Row
        #Add records
        self._db.execute("insert into  Ticket(Name,Gender,Comment) values(?,?,?)",(Name,Gender,Comment))
        self._db.commit()
        return ("Record is Added")


    def ListTickets(self):
        cursor=self._db.execute("select * from Ticket")
        return cursor



    def DeleteRecord(self,ID):
        self._db.row_factory=sqlite3.Row
        self._db.execute("delete from Ticket where ID={}".format(ID))
        self._db.commit()
        return ("Record is deleted")


    def UpdateRecord(self,ID,Comment):
        self._db.row_factory=sqlite3
        self._db.execute("update Ticket set Comments=? where ID=?"(Comment,ID))
        self._db.commit()
        return "Record is Updated"

