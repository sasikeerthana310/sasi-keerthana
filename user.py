import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("dbFile.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS user_info (accountno PRIMARYKEY text, holdername text, dob text, phone text, ifsccode text, depositamount text, withdrawalamount text, balance text)")

    def Update(self,accountno,holdername,dob,phone,ifsccode,depositamount,withdrawalamount,balance,):
        self.dbCursor.execute("UPDATE user_info SET holdername = ?, dob = ?, phone = ?, ifsccode=?, depositamount=?, withdrawalamount=?, balance=?  WHERE accountno = ?",(holdername,dob,phone,ifsccode,depositamount,withdrawalamount,balance,accountno,),)
        self.dbConnection.commit()

    def Search(self, accountno):
        self.dbCursor.execute("SELECT * FROM user_info WHERE accountno = ?", (accountno,))
        searchResults = self.dbCursor.fetchall()
        return searchResults


class Values:
    def Validate(self,accountno,holdername,dob,phone,ifsccode,depositamount,withdrawalamount,balance):
        if not (accountno.isdigit() and (len(accountno) == 11)):
            return "Account Number"
        elif not (holdername.isalpha()):
            return "Holder Name"
        elif not (phone.isdigit() and (len(phone) == 10)):
            return "Phone Number"
        elif not (ifsccode.isdigit()):
            return "IFSC Code"
        elif not depositamount.isdigit():
            return "Deposit Amount"
        elif not withdrawalamount.isdigit():
            return "Withdrawal Amount"
        elif not balance.isdigit():
            return "Balance"
        else:
            return "SUCCESS"

class UpdateWindow:
    def __init__(self, accountno):
        self.window = tkinter.Tk()
        self.window.wm_title("Update data")

        # Initializing all the variables
        self.accountno = accountno

        self.holdername = tkinter.StringVar()
        self.dob = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.ifsccode = tkinter.StringVar()
        self.depositamount = tkinter.StringVar()
        self.withdrawalamount = tkinter.StringVar()
        self.balance = tkinter.StringVar()

        # Labels
        tkinter.Label(self.window, text = "Account No",  width = 25).grid(pady = 5, column = 1, row = 1)
        tkinter.Label(self.window, text = accountno,  width = 25).grid(pady = 5, column = 3, row = 1)
        tkinter.Label(self.window, text = "Holder Name",  width = 25).grid(pady = 5, column = 1, row = 2)
        tkinter.Label(self.window, text = "D.O.B",  width = 25).grid(pady = 5, column = 1, row = 3)
        tkinter.Label(self.window, text = "Phone No",  width = 25).grid(pady = 5, column = 1, row = 4)
        tkinter.Label(self.window, text = "IFSC Code",  width = 25).grid(pady = 5, column = 1, row = 5)
        tkinter.Label(self.window, text = "Deposit Amount",  width = 25).grid(pady = 5, column = 1, row = 6)
        tkinter.Label(self.window, text = "Withdrawal Amount",  width = 25).grid(pady = 5, column = 1, row = 7)
        tkinter.Label(self.window, text = "Balance",  width = 25).grid(pady = 5, column = 1, row = 8)

        # Set previous values
        self.database = Database()
        self.searchResults = self.database.Search(accountno)

        tkinter.Label(self.window, text = self.searchResults[0][1],  width = 25).grid(pady = 5, column = 2, row = 2)
        tkinter.Label(self.window, text = self.searchResults[0][2],  width = 25).grid(pady = 5, column = 2, row = 3)
        tkinter.Label(self.window, text = self.searchResults[0][3],  width = 25).grid(pady = 5, column = 2, row = 4)
        tkinter.Label(self.window, text = self.searchResults[0][4],  width = 25).grid(pady = 5, column = 2, row = 5)
        tkinter.Label(self.window, text = self.searchResults[0][5],  width = 25).grid(pady = 5, column = 2, row = 6)
        tkinter.Label(self.window, text = self.searchResults[0][6],  width = 25).grid(pady = 5, column = 2, row = 7)
        tkinter.Label(self.window, text = self.searchResults[0][7],  width = 25).grid(pady = 5, column = 2, row = 8)

        # Fields
        # Entry widgets
        self.holdernameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.holdername)
        self.dobEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.dob)
        self.phoneEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.phone)
        self.ifsccodeEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.ifsccode)
        self.depositamountEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.depositamount)
        self.withdrawalamountEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.withdrawalamount)
        self.balanceEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.balance)

        self.holdernameEntry.grid(pady = 5, column = 3, row = 2)
        self.dobEntry.grid(pady = 5, column = 3, row = 3)
        self.phoneEntry.grid(pady = 5, column = 3, row = 4)
        self.ifsccodeEntry.grid(pady = 5, column = 3, row = 5)
        self.depositamountEntry.grid(pady = 5, column = 3, row = 6)
        self.withdrawalamountEntry.grid(pady = 5, column = 3, row = 7)
        self.balanceEntry.grid(pady = 5, column = 3, row = 8)

        # Button widgets
        tkinter.Button(self.window, width = 20, text = "Update", command = self.Update,  font='HarlowSolidItalic 14 bold italic',background = "dark blue",foreground="white").grid(pady = 15, padx = 5, column = 1, row = 14)
        tkinter.Button(self.window, width = 20, text = "Reset", command = self.Reset,  font='HarlowSolidItalic 14 bold italic',background = "dark blue",foreground="white").grid(pady = 15, padx = 5, column = 2, row = 14)
        tkinter.Button(self.window, width = 20, text = "Close", command = self.window.destroy,  font='HarlowSolidItalic 14 bold italic',background = "dark blue",foreground="white").grid(pady = 15, padx = 5, column = 3, row = 14)

        self.window.mainloop()

    def Update(self):
        self.database = Database()
        self.database.Update(self.accountno,self.holdernameEntry.get(), self.dobEntry.get(), self.phoneEntry.get(), self.ifsccodeEntry.get(),self.depositamountEntry.get(), self.withdrawalamountEntry.get(), self.balanceEntry.get())
        tkinter.messagebox.showinfo("Updated data", "Successfully updated the above data in the database")

    def Reset(self):
        self.holdernameEntry.delete(0, tkinter.END)
        self.dobEntry.delete(0, tkinter.END)
        self.phoneEntry.delete(0, tkinter.END)
        self.ifsccodeEntry.delete(0, tkinter.END)
        self.depositamountEntry.delete(0, tkinter.END)
        self.withdrawalamountEntry.delete(0, tkinter.END)
        self.balanceEntry.delete(0, tkinter.END)

class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        self.databaseViewWindow.wm_title("Database View")

        # Label widgets
        tkinter.Label(self.databaseViewWindow, text="Database View Window", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = ("accountno","holdername","dob","phone","ifsccode","depositamount","withdrawalamount","balance",)

        # Treeview column headings
        self.databaseView.heading("accountno", text="Account No")
        self.databaseView.heading("holdername", text="Holder Name")
        self.databaseView.heading("dob", text="D.O.B")
        self.databaseView.heading("phone", text="Phone Number")
        self.databaseView.heading("ifsccode", text="IFSC code")
        self.databaseView.heading("depositamount", text="Deposit Amount")
        self.databaseView.heading("withdrawalamount", text="Withdrawal Amount")
        self.databaseView.heading("balance", text="Balance")

        # Treeview columns
        self.databaseView.column("accountno", width=100)
        self.databaseView.column("holdername", width=100)
        self.databaseView.column("dob", width=100)
        self.databaseView.column("phone", width=100)
        self.databaseView.column("ifsccode", width=100)
        self.databaseView.column("depositamount", width=100)
        self.databaseView.column("withdrawalamount", width=100)
        self.databaseView.column("balance", width=100)

        for record in data:
            self.databaseView.insert("", "end", values=(record))

        self.databaseViewWindow.mainloop()


class SearchDeleteWindow:
    def __init__(self, task):
        window = tkinter.Tk()
        window.wm_title(task + " data")

        # Initializing all the variables
        self.accountno = tkinter.StringVar()
        self.holdername = tkinter.StringVar()
        self.heading = "Please enter User Account no to " + task

        # Labels
        tkinter.Label(window, text=self.heading, width=100).grid(pady=20, row=1)
        tkinter.Label(window, text="User Account No", width=100).grid(pady=5, row=2)

        # Entry widgets
        self.accountnoEntry = tkinter.Entry(window, width=50, textvariable=self.accountno)

        self.accountnoEntry.grid(pady=5, row=3)

        # Button widgets
        if task == "Search":
            tkinter.Button(window, width=20, text=task, command=self.Search,  font='HarlowSolidItalic 14 bold italic',background = "dark blue",foreground="white").grid(pady=15, padx=5, column=1, row=14)
        elif task == "Delete":
            tkinter.Button(window, width=20, text=task, command=self.Delete,  font='HarlowSolidItalic 14 bold italic',background = "dark blue",foreground="white").grid(pady=15, padx=5, column=1, row=14)

    def Search(self):
        self.database = Database()
        self.data = self.database.Search(self.accountnoEntry.get())
        self.databaseView = DatabaseView(self.data)

    def Delete(self):
        self.database = Database()
        self.database.Delete(self.accountnoEntry.get())
        tkinter.messagebox.showinfo("Deleted data", "Successfully deleted the above data from the database")


class HomePage:
    def login(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.wm_title("User Login")

        tkinter.Label(self.homePageWindow, text="Welcome User", width=100).grid(pady=20, column=1, row=1)

        # Label
        tkinter.Label(self.updateaccountnoWindow, text="USERNAME", width=100).grid(pady=20, row=1)
        tkinter.Label(self.updateaccountnoWindow, text="PASSWORD", width=100).grid(pady=20, row=1)

        # Entry widgets
        self.usernameEntry = tkinter.Entry(self.updateaccountnoWindow, width=50, textvariable=self.accountno)
        self.usernameEntry.grid(pady=10, row=2)
        self.passwordEntry = tkinter.Entry(self.updateaccountnoWindow, width=50, textvariable=self.accountno)
        self.passwordEntry.grid(pady=10, row=2)

        tkinter.Button(self.homePageWindow,width=20,text="Logout",command=self.homePageWindow.destroy, font='HarlowSolidItalic 14 bold italic',background = "dark blue",foreground="white").grid(pady=15, column=1, row=7)

        self.homePageWindow.mainloop()
    def __init__(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.wm_title("Users Information System")

        tkinter.Label(self.homePageWindow, text="Home Page", width=50, font='Algerian 30 bold', foreground="black").grid(pady=20, column=1, row=1)

        tkinter.Button(self.homePageWindow, width=20, text="My Account", command=self.Search,  font='HarlowSolidItalic 14 bold italic',background = "dark blue",foreground="white").grid(pady=15, column=1, row=4)
        tkinter.Button(self.homePageWindow, width=20, text="Update my Details", command=self.Update,  font='HarlowSolidItalic 14 bold italic',background = "dark blue",foreground="white").grid(pady=15, column=1, row=3)
        tkinter.Button(self.homePageWindow,width=20,text="Logout",command=self.homePageWindow.destroy,  font='HarlowSolidItalic 14 bold italic',background = "dark blue",foreground="white").grid(pady=15, column=1, row=7)

        self.homePageWindow.mainloop()

    def Update(self):
        self.updateaccountnoWindow = tkinter.Tk()
        self.updateaccountnoWindow.wm_title("Update data")

        # Initializing all the variables
        self.accountno = tkinter.StringVar()

        # Label
        tkinter.Label(self.updateaccountnoWindow, text="Enter the Account no to update", width=100).grid(pady=20, row=1)

        # Entry widgets
        self.accountnoEntry = tkinter.Entry(self.updateaccountnoWindow, width=50, textvariable=self.accountno)
        self.accountnoEntry.grid(pady=10, row=2)

        # Button widgets
        tkinter.Button(self.updateaccountnoWindow, width=20, text="Update", command=self.updateaccountno,  font='HarlowSolidItalic 14 bold italic',background = "dark blue",foreground="white").grid(pady=10, row=3)

        self.updateaccountnoWindow.mainloop()

    def updateaccountno(self):
        self.updateWindow = UpdateWindow(self.accountnoEntry.get())
        self.updateaccountnoWindow.destroy()

    def Search(self):
        self.searchWindow = SearchDeleteWindow("Search")

homePage = HomePage()
