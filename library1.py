from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # variable

        self.member_var=StringVar()
        self.reg_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.borrowdate_var=StringVar()
        self.duedate_var=StringVar()
        self.daysonbook_var=StringVar()
        self.laterreturnfine_var=StringVar()
        self.oveduedate_var=StringVar()
        self.finalprice_var=StringVar()




        # title - 1st box

        lbtitle=Label(self.root, text="Library Management System", bg="powder blue", fg="black",bd=20, relief=RIDGE, font=("times new roman",45,"bold"),padx=2,pady=6)
        lbtitle.pack(side=TOP,fill=X)

        # frame - 2nd box

        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=110,width=1280,height=380)

        #left frame

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information", bg="powder blue", fg="black",bd=15, relief=RIDGE, font=("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=4,width=600,height=340)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("arial",10,"bold"),padx=1,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember= ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),width=16,textvariable=self.member_var,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblreg_No=Label(DataFrameLeft,bg="powder blue",text="Reg No",font=("arial",10,"bold"),padx=1,pady=6)
        lblreg_No.grid(row=1,column=0,sticky=W)
        txtreg_No = Entry(DataFrameLeft,font=("arial",10),textvariable=self.reg_var,width=20)
        txtreg_No.grid(row=1,column=1)

        lblID_No=Label(DataFrameLeft,bg="powder blue",text="ID",font=("arial",10,"bold"),padx=1,pady=6)
        lblID_No.grid(row=2,column=0,sticky=W)
        txtID_No = Entry(DataFrameLeft,font=("arial",10),textvariable=self.id_var,width=20)
        txtID_No.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name",font=("arial",10,"bold"),padx=1,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName = Entry(DataFrameLeft,font=("arial",10),textvariable=self.firstname_var,width=20)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name",font=("arial",10,"bold"),padx=1,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName = Entry(DataFrameLeft,font=("arial",10),textvariable=self.lastname_var,width=20)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address 1",font=("arial",10,"bold"),padx=1,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1 = Entry(DataFrameLeft,font=("arial",10),textvariable=self.address1_var,width=20)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address 2",font=("arial",10,"bold"),padx=1,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2 = Entry(DataFrameLeft,font=("arial",10),textvariable=self.address2_var,width=20)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post Code",font=("arial",10,"bold"),padx=1,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode = Entry(DataFrameLeft,font=("arial",10),textvariable=self.postcode_var,width=20)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile",font=("arial",10,"bold"),padx=1,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile = Entry(DataFrameLeft,font=("arial",10),textvariable=self.mobile_var,width=20)
        txtMobile.grid(row=8,column=1)

        lblBookID=Label(DataFrameLeft,bg="powder blue",text="Book ID",font=("arial",10,"bold"),padx=1,pady=6)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID = Entry(DataFrameLeft,font=("arial",10),textvariable=self.bookid_var,width=20)
        txtBookID.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Category",font=("arial",10,"bold"),padx=1,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle = Entry(DataFrameLeft,font=("arial",10),textvariable=self.booktitle_var,width=20)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author",font=("arial",10,"bold"),padx=1,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor = Entry(DataFrameLeft,font=("arial",10),textvariable=self.author_var,width=20)
        txtAuthor.grid(row=2,column=3)

        lblBorrowDate=Label(DataFrameLeft,bg="powder blue",text="Borrow Date",font=("arial",10,"bold"),padx=1,pady=6)
        lblBorrowDate.grid(row=3,column=2,sticky=W)
        txtBorrowDate = Entry(DataFrameLeft,font=("arial",10),textvariable=self.borrowdate_var,width=20)
        txtBorrowDate.grid(row=3,column=3)

        lblDueDate=Label(DataFrameLeft,bg="powder blue",text="Due Date",font=("arial",10,"bold"),padx=1,pady=6)
        lblDueDate.grid(row=4,column=2,sticky=W)
        txtDueDate = Entry(DataFrameLeft,font=("arial",10),textvariable=self.duedate_var,width=20)
        txtDueDate.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book",font=("arial",10,"bold"),padx=1,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysonBook = Entry(DataFrameLeft,font=("arial",10),textvariable=self.daysonbook_var,width=20)
        txtDaysonBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine",font=("arial",10,"bold"),padx=1,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft,font=("arial",10),textvariable=self.laterreturnfine_var,width=20)
        txtLateReturnFine.grid(row=6,column=3)

        lblDayOverDate=Label(DataFrameLeft,bg="powder blue",text="Date Over Due",font=("arial",10,"bold"),padx=1,pady=6)
        lblDayOverDate.grid(row=7,column=2,sticky=W)
        txtDayOverDate = Entry(DataFrameLeft,font=("arial",10),textvariable=self.oveduedate_var,width=20)
        txtDayOverDate.grid(row=7,column=3)

        lblFinalPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price",font=("arial",10,"bold"),padx=1,pady=6)
        lblFinalPrice.grid(row=8,column=2,sticky=W)
        txtFinalPrice = Entry(DataFrameLeft,font=("arial",10),textvariable=self.finalprice_var,width=20)
        txtFinalPrice.grid(row=8,column=3)



        # Data frame Right


        DataFrameRight=LabelFrame(frame,text="Book Details", bg="powder blue", fg="black",bd=15, relief=RIDGE, font=("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameRight.place(x=630,y=5,width=590,height=340)

        self.txtBox=Text(DataFrameRight,font=("times new roman",12),width=45,height=14,padx=2,pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollBar=Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0,column=1,sticky="ns")

        listBooks=["It Ends With Us", "Ugly Love", "November 9", "Maybe Someday", "All Your Perfects", "Maybe Not", 
                                                   "Without Merit", "Slammed", "Point Of Retreat", 
                                                   "Verity", "Confess", "Losing Hope"]
        
        def SelectBook(events=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="It Ends With Us"):
                self.bookid_var.set("BK001")
                self.booktitle_var.set("Novel")
                self.author_var.set("Colleen Hoover")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(10)
                self.laterreturnfine_var.set("Rs.50")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.500")

            elif(x=="Ugly Love"):
                self.bookid_var.set("BK002")
                self.booktitle_var.set("Novel")
                self.author_var.set("Colleen Hoover")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterreturnfine_var.set("Rs.5")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.50")

            elif(x=="November 9"):
                self.bookid_var.set("BK003")
                self.booktitle_var.set("Novel")
                self.author_var.set("Colleen Hoover")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterreturnfine_var.set("Rs.50")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif(x=="Maybe Someday"):
                self.bookid_var.set("BK004")
                self.booktitle_var.set("Novel")
                self.author_var.set("Colleen Hoover")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterreturnfine_var.set("Rs.25")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.250")

            elif(x=="All Your Perfects"):
                self.bookid_var.set("BK005")
                self.booktitle_var.set("Novel")
                self.author_var.set("Colleen Hoover")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(1)
                self.laterreturnfine_var.set("Rs.40")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.400")

            elif(x=="Maybe Not"):
                self.bookid_var.set("BK006")
                self.booktitle_var.set("Novel")
                self.author_var.set("Colleen Hoover")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterreturnfine_var.set("Rs.55")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.550")

            elif(x=="Without Merit"):
                self.bookid_var.set("BK007")
                self.booktitle_var.set("Novel")
                self.author_var.set("Colleen Hoover")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(10)
                self.laterreturnfine_var.set("Rs.65")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.650")

            elif(x=="Slammed"):
                self.bookid_var.set("BK008")
                self.booktitle_var.set("Novel")
                self.author_var.set("Colleen Hoover")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(5)
                self.laterreturnfine_var.set("Rs.15")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.150")

            elif(x=="Point Of Retreat"):
                self.bookid_var.set("BK009")
                self.booktitle_var.set("Novel")
                self.author_var.set("Colleen Hoover")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(10)
                self.laterreturnfine_var.set("Rs.5")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.50")

            elif(x=="Verity"):
                self.bookid_var.set("BK010")
                self.booktitle_var.set("Novel")
                self.author_var.set("Colleen Hoover")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(20)
                self.laterreturnfine_var.set("Rs.80")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.800")

            elif(x=="Confess"):
                self.bookid_var.set("BK011")
                self.booktitle_var.set("Novel")
                self.author_var.set("Colleen Hoover")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(1)
                self.laterreturnfine_var.set("Rs.30")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.30")

            elif(x=="Losing Hope"):
                self.bookid_var.set("BK011")
                self.booktitle_var.set("Novel")
                self.author_var.set("Colleen Hoover")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(10)
                self.laterreturnfine_var.set("Rs.45")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.450")

            

            
        
        
        listBox=Listbox(DataFrameRight,width=25,height=17)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollBar.config(command=listBox.yview)

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection))
            x=value
            if(x=="It Ends With Us"):
                self.bookid_var.set("001")
                self.booktitle_var.set("It Ends With Us")
                self.author_var.set("Colleen Hoover")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var(d1)
                self.duedate_var(d3)
                self.daysonbook_var(15)
                self.laterreturnfine_var("Rs.20")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.788")

            elif(x=="Ugly Love"):
                self.bookid_var.set("001")
                self.booktitle_var.set("It Ends With Us")
                self.author_var.set("Colleen Hoover")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var(d1)
                self.duedate_var(d3)
                self.daysonbook_var(15)
                self.laterreturnfine_var("Rs.20")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.788")

            elif(x=="November 9"):
                self.bookid_var.set("001")
                self.booktitle_var.set("It Ends With Us")
                self.author_var.set("Colleen Hoover")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var(d1)
                self.duedate_var(d3)
                self.daysonbook_var(15)
                self.laterreturnfine_var("Rs.20")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.788")

            elif(x=="Maybe Someday"):
                self.bookid_var.set("001")
                self.booktitle_var.set("It Ends With Us")
                self.author_var.set("Colleen Hoover")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var(d1)
                self.duedate_var(d3)
                self.daysonbook_var(15)
                self.laterreturnfine_var("Rs.20")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.788")

            elif(x=="All Your Perfects"):
                self.bookid_var.set("001")
                self.booktitle_var.set("It Ends With Us")
                self.author_var.set("Colleen Hoover")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var(d1)
                self.duedate_var(d3)
                self.daysonbook_var(15)
                self.laterreturnfine_var("Rs.20")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.788")

            elif(x=="Verity"):
                self.bookid_var.set("001")
                self.booktitle_var.set("It Ends With Us")
                self.author_var.set("Colleen Hoover")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var(d1)
                self.duedate_var(d3)
                self.daysonbook_var(15)
                self.laterreturnfine_var("Rs.20")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.788")

            elif(x=="Confess"):
                self.bookid_var.set("001")
                self.booktitle_var.set("It Ends With Us")
                self.author_var.set("Colleen Hoover")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var(d1)
                self.duedate_var(d3)
                self.daysonbook_var(15)
                self.laterreturnfine_var("Rs.20")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.788")

            elif(x=="Slammed"):
                self.bookid_var.set("001")
                self.booktitle_var.set("It Ends With Us")
                self.author_var.set("Colleen Hoover")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var(d1)
                self.duedate_var(d3)
                self.daysonbook_var(15)
                self.laterreturnfine_var("Rs.20")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.788")

            elif(x=="Without Merit"):
                self.bookid_var.set("001")
                self.booktitle_var.set("It Ends With Us")
                self.author_var.set("Colleen Hoover")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var(d1)
                self.duedate_var(d3)
                self.daysonbook_var(15)
                self.laterreturnfine_var("Rs.20")
                self.oveduedate_var.set("No")
                self.finalprice_var.set("Rs.788")

        for item in listBooks:
            listBox.insert(END,item)





        #Button - 3rd box

        FrameButton = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameButton.place(x=0,y=490,width=1280,height=59)

        btnAddData=Button(FrameButton,command=self.add_data,text="Add Data",font=("times new roman",12),width=21,bg="black",fg="white")
        btnAddData.grid(row=0,column=0)

        btnShowData=Button(FrameButton,command=self.show_data,text="Show Data",font=("times new roman",12),width=21,bg="black",fg="white")
        btnShowData.grid(row=0,column=1)

        btnUpdate=Button(FrameButton,command=self.update_data,text="Update",font=("times new roman",12),width=21,bg="black",fg="white")
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(FrameButton,command=self.delete,text="Delete",font=("times new roman",12),width=21,bg="black",fg="white")
        btnDelete.grid(row=0,column=3)

        btnReset=Button(FrameButton,command=self.reset,text="Reset",font=("times new roman",12),width=21,bg="black",fg="white")
        btnReset.grid(row=0,column=4)

        btnExit=Button(FrameButton,command=self.iExit,text="Exit",font=("times new roman",12),width=21,bg="black",fg="white")
        btnExit.grid(row=0,column=5)

        # Information - 4th box

        FrameDetails = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=549,width=1280,height=148)

        Table_frame = Frame(FrameDetails,bd=6,relief=RIDGE,padx=20,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1220,height=120)

        xscroll=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","regno","title","firstname","lastname","address1",
                                                             "address2","postid","mobile","bookid","booktitle","author",
                                                             "borrowdate","daysonbook","duedate","latereturnfine","dateoverdue","finalprice"),
                                                             xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)



        self.library_table.heading("membertype",text = "Member Type")
        self.library_table.heading("regno",text = "Reg No")
        self.library_table.heading("title",text = "ID")
        self.library_table.heading("firstname",text = "First Name")
        self.library_table.heading("lastname",text = "Last Name")
        self.library_table.heading("address1",text = "Address 1")
        self.library_table.heading("address2",text = "Address 2")
        self.library_table.heading("postid",text = "Post ID")
        self.library_table.heading("mobile",text = "Mobile Number")
        self.library_table.heading("bookid",text = "Book ID")
        self.library_table.heading("booktitle",text = "Book Category")
        self.library_table.heading("author",text = "Author")
        self.library_table.heading("borrowdate",text = "Borrow Date")
        self.library_table.heading("duedate",text = "Due Date")
        self.library_table.heading("daysonbook",text = "Days On Book")
        self.library_table.heading("latereturnfine",text = "Late Return Fine")
        self.library_table.heading("dateoverdue",text = "Over Due Date")
        self.library_table.heading("finalprice",text = "Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("regno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("borrowdate",width=100)
        self.library_table.column("duedate",width=100)
        self.library_table.column("daysonbook",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)



    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jeya@2023sql",database="mydata")  
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.reg_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.borrowdate_var.get(),
                                                                                                                self.duedate_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.laterreturnfine_var.get(),
                                                                                                                self.oveduedate_var.get(),
                                                                                                                self.finalprice_var.get()
        ))
        conn.commit()
        self.fetch_data
        conn.close()

        messagebox.showinfo("Success","Member added successfully")

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jeya@2023sql",database="mydata")  
        my_cursor=conn.cursor()
        my_cursor.execute("update library1 set Member_Type=%s,ID=%s,First_Name=%s,Last_Name=%s,Address_1=%s,Address_2=%s,Post_ID=%s,Mobile=%s,Book_ID=%s,Category=%s,Author=%s,Borrow_Date=%s,Due_Date=%s,Days_On_Book=%s,Late_Return_Fine=%s,Due_Over_Date=%s,Final_Price=%s where Reg_No=%s",(
                                                                                                                self.member_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.borrowdate_var.get(),
                                                                                                                self.duedate_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.laterreturnfine_var.get(),
                                                                                                                self.oveduedate_var.get(),
                                                                                                                self.finalprice_var.get(),
                                                                                                                self.reg_var.get(),
                                                                                                                                      
        ))

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Successfully updated!")  
    

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jeya@2023sql",database="mydata")  
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library1")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,events=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0])
        self.reg_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.author_var.set(row[11])
        self.borrowdate_var.set(row[12])
        self.duedate_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.laterreturnfine_var.set(row[15])
        self.oveduedate_var.set(row[16])
        self.finalprice_var.set(row[17])

    def show_data(self):
        self.txtBox.insert(END,"Member Type:\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END,"Register Number:\t" + self.reg_var.get() + "\n")
        self.txtBox.insert(END,"Student ID:\t" + self.id_var.get() + "\n")  
        self.txtBox.insert(END,"First Name:\t" + self.firstname_var.get() + "\n")       
        self.txtBox.insert(END,"Last Name:\t" + self.lastname_var.get() + "\n")  
        self.txtBox.insert(END,"Address 1:\t" + self.address1_var.get() + "\n")  
        self.txtBox.insert(END,"Address 2:\t" + self.address2_var.get() + "\n")  
        self.txtBox.insert(END,"Post Code:\t" + self.postcode_var.get() + "\n")  
        self.txtBox.insert(END,"Mobile:\t" + self.mobile_var.get() + "\n")  
        self.txtBox.insert(END,"Book ID:\t" + self.bookid_var.get() + "\n")  
        self.txtBox.insert(END,"Category:\t" + self.booktitle_var.get() + "\n")  
        self.txtBox.insert(END,"Author:\t" + self.author_var.get() + "\n")  
        self.txtBox.insert(END,"Borrow Date:\t" + self.borrowdate_var.get() + "\n")  
        self.txtBox.insert(END,"Due Date:\t" + self.duedate_var.get() + "\n")  
        self.txtBox.insert(END,"Days On Book:\t" + self.daysonbook_var.get() + "\n")  
        self.txtBox.insert(END,"Late return Fine:\t" + self.laterreturnfine_var.get() + "\n")  
        self.txtBox.insert(END,"Over Due Date:\t" + self.oveduedate_var.get() + "\n")  
        self.txtBox.insert(END,"Final Price:\t" + self.finalprice_var.get() + "\n")  


    def delete(self):
        if self.reg_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","Select member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="jeya@2023sql",database="mydata")  
            my_cursor=conn.cursor()
            query="delete from library1 where Reg_No=%s"
            value=(self.reg_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member deleted successfully!")
    
    def reset(self):
        self.member_var.set(""),
        self.reg_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.borrowdate_var.set(""),
        self.duedate_var.set(""),
        self.daysonbook_var.set(""),
        self.laterreturnfine_var.set(""),
        self.oveduedate_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete(1.0,END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Are you sure  you want to exit?")
        if iExit>0:
            self.root.destroy()
            return 










    



if __name__ == "__main__":
    root=Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()