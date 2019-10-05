from CMS_UsingList_PureOOP_Pickle_ExceptionDataBAse import Customer
from tkinter import  *
import tkinter.messagebox
import tkinter.filedialog
tempIndex=0
def exportAllCustomerInCSV():
    filename=tkinter.filedialog.asksaveasfilename()
    fs=open(filename,'w')
    columns=["Id","Name","Address","Mobile No"]
    for i in range(len(columns)):
        fs.write(columns[i]+",")
    fs.write("\n")
    rowno=1
    for e in Customer.listCus:
        cusInDict=e.__dict__
        columnno=0
        for e1 in cusInDict.values():
            fs.write(str(e1)+",")
        fs.write("\n")
    fs.close()

def showCustomerByIndex(i):
    cus=Customer.listCus[i]
    varId.set(cus.id)
    varName.set(cus.name)
    varAddress.set(cus.address)
    varMob.set(cus.mob)
def showAllCustomerNew(top):
    columns=["Id","Name","Address","Mobile No"]
    for i in range(len(columns)):
        lbl1=Label(master=top,text=columns[i])
        lbl1.grid(row=0,column=i)
    rowno=1
    for e in Customer.listCus:
        cusInDict=e.__dict__
        columnno=0
        for e1 in cusInDict.values():
            var1=StringVar()
            txt1=Entry(master=top,textvariable=var1)
            txt1.grid(row=rowno,column=columnno)
            var1.set(e1)
            columnno+=1
        rowno+=1




def showAllCustomer(top):
    columns=["Id","Name","Address","Mobile No"]
    for i in range(len(columns)):
        lbl1=Label(master=top,text=columns[i])
        lbl1.grid(row=0,column=i)
    rowno=1
    for e in Customer.listCus:
        var1=IntVar()
        txt1=Entry(master=top,textvariable=var1)
        txt1.grid(row=rowno,column=0)
        var1.set(e.id)

        var2 = StringVar()
        txt2 = Entry(master=top, textvariable=var2)
        txt2.grid(row=rowno, column=1)
        var2.set(e.name)

        var3 = StringVar()
        txt3 = Entry(master=top, textvariable=var3)
        txt3.grid(row=rowno, column=2)
        var3.set(e.address)

        var4 = StringVar()
        txt4 = Entry(master=top, textvariable=var4)
        txt4.grid(row=rowno, column=3)
        var4.set(e.mob)
        rowno+=1
#Code for Handler Start from Here
def btnAdd_Click():
    try:
        cus = Customer()
        cus.id = varId.get()
        cus.name = varName.get()
        cus.address = varAddress.get()
        cus.mob = varMob.get()
        cus.addCustomer()
        tkinter.messagebox.showinfo("Sucess","Customer Added Sucessfully")
    except Exception as ex:
        tkinter.messagebox.showerror("Error", ex)
def btnSearch_Click():
    try:
        id = varId.get()
        cus = Customer()
        cus.searchCustomer(id)
        varName.set(cus.name)
        varAddress.set(cus.address)
        varMob.set(cus.mob)
    except Exception as ex:
        tkinter.messagebox.showerror("Error", ex)

def btnDelete_Click():
    try:
        id = varId.get()
        cus = Customer()
        cus.deleteCustomer(id)
        tkinter.messagebox.showinfo("Sucess","Customer Deleted Sucessfully")
    except Exception as ex:
        tkinter.messagebox.showerror("Error", ex)


def btnModify_Click():
    try:
        cus = Customer()
        id = varId.get()
        cus.name = varName.get()
        cus.address = varAddress.get()
        cus.mob = varMob.get()
        cus.modifyCustomer(id)
        tkinter.messagebox.showinfo("Sucess", "Customer Modified Sucessfully")
    except Exception as ex:
        tkinter.messagebox.showerror("Error", ex)

def btnFirst_Click():
    global tempIndex
    tempIndex=0
    showCustomerByIndex(tempIndex)
def btnPrev_Click():
    global tempIndex
    if(tempIndex>0):
        tempIndex-=1
    showCustomerByIndex(tempIndex)
def btnNext_Click():
    global tempIndex
    if (tempIndex < len(Customer.listCus)-1):
        tempIndex += 1
    showCustomerByIndex(tempIndex)
def btnLast_Click():
    global tempIndex
    tempIndex = len(Customer.listCus)-1
    showCustomerByIndex(tempIndex)
def btnSaveAll_Click():
    Customer.saveDatainFile()
    tkinter.messagebox.showinfo("Sucess", "Customer Saved Sucessfully")
def btnLoadAll_Click():
    Customer.loadDataFromFile()
    tkinter.messagebox.showinfo("Sucess","Customer Loaded Sucessfully")
def btnShowAll_Click():
    top=Toplevel()
    showAllCustomerNew(top)
def btnExportAll_Click():
    exportAllCustomerInCSV()
#Code for Handler Ends Here
root=Tk()
lblId=Label(master=root,text="Id",width=16)
lblId.grid(row=0,column=0,columnspan=2)

lblName=Label(master=root,text="Name",width=16)
lblName.grid(row=1,column=0,columnspan=2)

lblAddress=Label(master=root,text="Address",width=16)
lblAddress.grid(row=2,column=0,columnspan=2)

lblMob=Label(master=root,text="Mobile No",width=16)
lblMob.grid(row=3,column=0,columnspan=2)

varId=IntVar()
txtId=Entry(master=root,textvariable=varId,width=16)
txtId.grid(row=0,column=2,columnspan=2)

varName=StringVar()
txtName=Entry(master=root,textvariable=varName,width=16)
txtName.grid(row=1,column=2,columnspan=2)

varAddress=StringVar()
txtAddress=Entry(master=root,textvariable=varAddress,width=16)
txtAddress.grid(row=2,column=2,columnspan=2)

varMob=StringVar()
txtMob=Entry(master=root,textvariable=varMob,width=16)
txtMob.grid(row=3,column=2,columnspan=2)

btnAdd=Button(master=root,text="Add",width=8,command=btnAdd_Click)
btnAdd.grid(row=4,column=0)

btnSearch=Button(master=root,text="Search",width=8,command=btnSearch_Click)
btnSearch.grid(row=4,column=1)

btnDelete=Button(master=root,text="Delete",width=8,command=btnDelete_Click)
btnDelete.grid(row=4,column=2)

btnModify=Button(master=root,text="Modify",width=8,command=btnModify_Click)
btnModify.grid(row=4,column=3)


btnFirst=Button(master=root,text="First",width=8,command=btnFirst_Click)
btnFirst.grid(row=5,column=0)

btnPrev=Button(master=root,text="Previous",width=8,command=btnPrev_Click)
btnPrev.grid(row=5,column=1)

btnNext=Button(master=root,text="Next",width=8,command=btnNext_Click)
btnNext.grid(row=5,column=2)

btnLast=Button(master=root,text="Last",width=8,command=btnLast_Click)
btnLast.grid(row=5,column=3)

btnSaveAll=Button(master=root,text="Save in File",width=16,command=btnSaveAll_Click)
btnSaveAll.grid(row=6,column=0,columnspan=2)

btnLoadAll=Button(master=root,text="Load from File",width=16,command=btnLoadAll_Click)
btnLoadAll.grid(row=6,column=2,columnspan=2)

btnShowAll=Button(master=root,text="Show All Customer",width=32,command=btnShowAll_Click)
btnShowAll.grid(row=7,column=0,columnspan=4)

btnExportAll=Button(master=root,text="Export All Customer",width=32,command=btnExportAll_Click)
btnExportAll.grid(row=8,column=0,columnspan=4)



root.mainloop()
