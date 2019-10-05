#BLL Code Start From Here
import pymysql
class Customer:
    con = pymysql.connect(host="localhost", user="root", password='root123', database='12thjune')
    listCus=[]
    def __init__(self):
        self.id=0
        self.name=""
        self.address=""
        self.mob=""

    def __str__(self):
        return "Id: "+str(self.id)+" Name:"+self.name+" Address:"+self.address+" Mobile No:"+self.mob

    def addCustomer(self):
        myCursor = Customer.con.cursor()
        strQuery = "insert into customer values(%s,%s,%s,%s)"
        myCursor.execute(strQuery, (self.id, self.name, self.address, self.mob))
        Customer.con.commit()


    def searchCustomer(self,id):
        myCursor = Customer.con.cursor()
        strQuery = "select * from customer where id=%s"
        rowAffected=myCursor.execute(strQuery, (id))
        if(rowAffected!=0):
            row=myCursor.fetchone()
            self.id = row[0]
            self.name = row[1]
            self.address = row[2]
            self.mob = row[3]
        else:
            raise Exception("Id not found")

    def deleteCustomer(self,id):
        myCursor = Customer.con.cursor()
        strQuery = "delete from customer where id=%s"
        rowAffected = myCursor.execute(strQuery, (id))
        if (rowAffected != 0):
            Customer.con.commit()
        else:
            raise Exception("Id not found")

    def modifyCustomer(self,id):
        myCursor = Customer.con.cursor()
        strQuery = "update customer set name=%s,address=%s,mob=%s where id=%s"
        rowAffected=myCursor.execute(strQuery, ( self.name, self.address, self.mob,id))
        if (rowAffected != 0):
            Customer.con.commit()
        else:
            raise Exception("Id not found")

    @staticmethod
    def showAllCustomer():
        for e in Customer.listCus:
            print(e)
#BLL Code End Here

#PL Code Start From Here
if(__name__=="__main__"):
    while(True):
        print("1.Add Customer\n2.Search Customer\n3.Delete\n4.Modify\n5.ShowAll\n6.Save Data in File\n7.Load Data from File\n0.Exit")
        ch=input("Enter your choice")
        if(ch=='1'):
            try:
                cus=Customer()
                cus.id=int(input("Enter ID"))
                cus.name=input("Enter Name")
                cus.address=input("Enter Address")
                cus.mob=input("Enter Mobile no")
                cus.addCustomer()
                print("Customer Added Sucessfully")
            except Exception as ex:
                print(ex)
            #Write Code for Add Customer

        elif(ch=='2'):
            #Write Code for Search Customer
            try:
                id=int(input("Enter ID"))
                cus=Customer()
                cus.searchCustomer(id)
                print(cus)
                # print("Id:", cus.id, "Name:", cus.name, "address", cus.address, "mobile No",cus.mob)#Wrong code because list is not available in PL
            except Exception as ex:
                print(ex)


        elif(ch=='3'):

            #Write Code for Delete Customer
            try:
                id = int(input("Enter ID"))
                cus=Customer()
                cus.deleteCustomer(id)
                print("Customer Deleted Sucessfully")
            except Exception as ex:
                print(ex)

        elif(ch=='4'):
            try:
                cus = Customer()
                id = int(input("Enter ID"))
                cus.name = input("Enter Name")
                cus.address = input("Enter Address")
                cus.mob = input("Enter Mobile no")
                cus.modifyCustomer(id)
                print("Customer Modified Sucessfully")
            except Exception as ex:
                print(ex)
        elif(ch=='5'):
            Customer.showAllCustomer()
            #Write Code for Show All Customer
            pass
        elif (ch == '6'):
            Customer.saveDatainFile()

        elif (ch == '7'):
            Customer.loadDataFromFile()
            # Write Code for Show All Customer

        else:
            break


#PL Code End Here