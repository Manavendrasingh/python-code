#costumer managment system using oops

#BLL(business logic layer)
class costumer:
    listcos=[]
    def __init__(self):
        self.id=0
        self.age=0
        self.name=0
        self.phoneno=0
    def addCostumer(self):
        costumer.listcos.append(self)

    def searchCostumer(self):
        for e in costumer.listcos:
            if e.id==self.id:
                self.age=e.age
                self.name=e.name
                self.phoneno=e.phoneno
            return 1
        return 0
    def modifyCostumer(self):
        for e in costumer.listcos:
            if e.id==self.id:
                e.age=self.age
                e.name=self.name
                e.phoneno=self.phoneno
            return 1
        return 0
    def deletCostumer(self):
        for e in costumer.listcos:
            if e.id==self.id:
                costumer.listcos.remove(e)
            return 1
        return 0

#PL(priniple layer)
while(1) :
    print("enter the choice 1 for addcost, 2 for searchcost,3 for modifycost, 4 for delet cost, 5 for display cost,6 for exit")
    ch = input("enter")
    if ch=="1":#add costumer
        cos=costumer()
        cos.id=input("enter the costumer id")
        cos.age=input("eter the costumer age")
        cos.name=input("enter the costumer namme")
        cos.phoneno=input("enter the costumer mobile no")
        cos.addCostumer()
        print("costumer add successfully")

    elif ch=="2":#search costumer
        cos=costumer()
        cos.id=input("enter the costmer id for search")
        flag=cos.searchCostumer()
        if flag==1:
            print("costid=",cos.id,"costage=",cos.age,"costname=",cos.name,"costphoneno=",cos.phoneno)
        else:
            print("costumer not found")
    elif ch=="3" :#modify costumer
        cos=costumer()
        cos.id=input("enter the costumer id")
        cos.age=input("ente the updated age")
        cos.name=input('ente the updated name')
        cos.phoneno=input("enterht eupadated mobile no")
        flag=cos.modifyCostumer()
        if flag==1:
            print("costumer modify successfully")
        else:
            print("costuemr not found")

    elif ch=="4":#to delet costumer
        cos=costumer()
        cos.id=input("enter the costumer id")
        flag=cos.deletCostumer()
        if flag==1:
            print("costumer delet successfully")
        else:
            print("costumer not found")
    elif ch=="5":#diplay
        for cos in costumer.listcos:
            print("costid=", cos.id, "costage=", cos.age, "costname=", cos.name, "costphoneno=", cos.phoneno)

    elif ch=="6":
        break

    else :
        print("invaild choice")

























