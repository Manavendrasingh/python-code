#BLL Start
dictCus={}
def addCustomer(id, name, address, mob):
    l1=[]
    l1.append(id)
    l1.append(name)
    l1.append(address)
    l1.append(mob)
    dictCus[id]=l1
def searchCustomer(id):
    l1=dictCus[id]
    print("Id:",l1[0],"Name:",l1[1],"address",l1[2],"mobile No",l1[3])#Wrong Code(Using print in BLL)

def modifyCustomer(id,name='NA',address='NA',mob='NA'):
        l1 = dictCus[id]
        if(name!='NA'):
            l1[1]=name
        if(address!='NA'):
            l1[2]=address
        if(mob!='NA'):
            l1[3]=mob




def deleteCustomer(id):
    if(listId.__contains__(id)):
        i=listId.index(id)
        listId.pop(i)
        listName.pop(i)
        listAddess.pop(i)
        listMob.pop(i)
    else:
        print("Id not found")#Wrong Code(Using print in BLL)




#BLL End
#PL Start
while(True):
    print("1.Add Customer\n2.Search Customer\n3.Delete\n4.Modify\n5.ShowAll\n0.Exit")
    ch=input("Enter your choice")
    if(ch=='1'):
        print("Selection is 1")
        id=int(input("Enter ID"))
        name=input("Enter Name")
        address=input("Enter Address")
        mob=input("Enter Mobile no")
        addCustomer(id,name,address,mob)
        print("Customer Added Sucessfully")
        #Write Code for Add Customer
        pass
    elif(ch=='2'):
        print("Selection is 2")
        #Write Code for Search Customer
        id=int(input("Enter ID"))
        searchCustomer(id)
        # print("Id:", listId[i], "Name:", listName[i], "address", listAddess[i], "mobile No",listMob[i])#Wrong code because list is not available in PL

        pass
    elif(ch=='3'):
        print("Selection is 3")
        #Write Code for Delete Customer
        id = int(input("Enter ID"))
        deleteCustomer(id)
        print("Customer Deleted Sucessfully")

        pass
    elif(ch=='4'):
        print("Selection is 4")
        #Write Code for Modify Customer
        id = int(input("Enter ID"))
        print("1.Modify Name\n2Modify Address\n3.Modify Mobile No\n4.All Modify")
        ch1=input("Enter your choice")
        if(ch1=='4'):
            name = input("Enter Name")
            address = input("Enter Address")
            mob = input("Enter Mobile no")
            modifyCustomer(id,name,address,mob)
            pass
        elif(ch1=='1'):
            name = input("Enter Name")
            modifyCustomer(id, name=name)
            pass
        elif (ch1 == '2'):

            address = input("Enter Address")

            modifyCustomer(id, address=address)
            pass
        elif (ch1 == '3'):
            mob = input("Enter Mobile no")
            modifyCustomer(id, mob=mob)
            pass
    elif(ch=='5'):
        print("Selection is 5")
        #Write Code for Show All Customer
        pass
    else:
        break

        #Write code for Exit


#PL End