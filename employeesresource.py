#BLL


class Employees:#employee classs
    listemp = []
    def __init__(self):
        self.id = 0
        self.age = 0
        self.name = 0
        self.type = 0
    def addEmployee(self):
        Employees.listemp.append(self)
    @staticmethod
    def returntype(id):
        for e in Employees.listemp :
            if e.id == id:
                if e.type == "Director":
                    return Director()
                elif e.type == "manager":
                    return Manager()
                elif e.type == "Trainer":
                    return Trainer()
            else :
                return 0


    def SearchEmployee(self):
        for e in Employees.listemp :
            if e.id == self.id:
                self.age = e.age
                self.name = e.name
                self.type = e.type
    def ModifyEmployee(self):
        for e in Employees.listemp:
            if e.id == self.id:
                e.name = self.name
                e.age = self.age
    @staticmethod
    def returnobject(id):
        for e in Employees.listemp:
            if e.id == self.id:
                return e



class Manager(Employees): #Manager class
    def __init__(self):
        self.area = 0
        super().__init__()
    def addManager(self):
         super().addEmployee()
    def SearchEmployee(self):
        for e in Employees.listemp :
            if e.id == self.id:
                self.area == e.area
                super().SearchEmployee()
    def deleteEmployee(self):
        return self.type
        Employees.listemp.remove(self)
    def ModifyEmployee(self):
        for e in Employees.listemp :
            if e.id == self.id:
                 e.area = self.area
            super().ModifyEmployee()




class Director(Employees):#drector classs
    def __init__(self):
        self.share = 0
        super().__init__()
    def addDirector(self):
        super().addEmployee()
    def SearchEmployee(self):
        for e in Employees.listemp :
            if e.id == self.id:
                self.share == e.share
                super().SearchEmployee()

    def deleteEmployee(self):
        return self.type
        Employees.listemp.remove(self)

    def ModifyEmployee(self):
        for e in Employees.listemp:
            if e.id == self.id:
                e.share = self.share
                super().ModifyEmployee()





class Trainer(Employees):
    def __init__(self):
        self.course = 0
        super().__init__()
    def SearchEmployee(self):
        for e in Employees.listemp :
            if e.id == self.id:
                self.course == e.course
                super().SearchEmployee()

    def deleteEmployee(self):
        return self.type
        Employees.listemp.remove(self)

    def ModifyEmployee(self):
        for e in Employees.listemp:
            if e.id == self.id:
                e.course = self.course
            super().ModifyEmployee()





#PL




while(True):
    print("enter 1 gor add ,2 for search ,3 for delete , 4 for modify ,5 for display , 6 for exit")
    ch = input("enter the choice")
    if ch == '1':
        print("enter 1 for adding director ,2 for manager ,3 for Trainer ")
        cht = input("enter the choice")
        if cht == '1':#add director
                dr = Director()
                dr.id = input("enter the director id")
                dr.age = input("enter the director age")
                dr.name = input("enter the director name")
                dr.share = input("enter the director share")
                dr.type = "Director"
                dr.addDirector()
                print("Directer  added successfully")
        elif cht == '2':#add Manager
                mg = Manager()
                mg.id = input("enter the manager id")
                mg.age = input("enter the manager age")
                mg.name = input("enter the manager name")
                mg.area = input("enter the manager area")
                mg.type = "Manager"
                mg.addManager()
                print("manager  added successfully")
        elif cht == '3':#add trainer
                tr = Trainer()
                tr.id = input("enter the Trainer id")
                tr.age = input("enter the Trainer age")
                tr.name = input("enter the Trainer name")
                tr.course = input("enter the Trainer course")
                tr.type = "Manager"
                tr.addTrainer()
                print("Trainer  added successfully")

    elif ch == '2': #searchEmployee
        id = input("enter the id of employee")
        ob = Employees.returntype(id)
        if ob == 0:
            print("Employee no found")

        ob.SearchEmployee()
        ob.showEmployee()

    elif ch == '3':#delete Employee
        id = input("enter the id for deletetion ")
        ob = Employees.returntype(id)
        if ob == 0:
            print("Employee no found")
        type = ob.deleteEmployee()
        if type == "Director":
            print("Director delete successfully")
        elif type == "Manager":
            print("Manager delete successfully")
        elif type == "Trainer":
            print("Trainer delete successfully")
    elif ch == '4':#modify Employee
        id = input("enter the id for modification of employee")
        ob = Employees.returntype(id)
        if ob == 0:
            print("Employee no found")
        ob.age = input("enter the updataed age")
        ob.name = input(" enter the updataed name")
        if ob.type == "Director":
            ob.share = input("enter the updataed share")
        elif ob.type == "Manager":
            ob.share = input("enter the updataed area")
        elif ob.type == "Trainer":
            ob.share = input("enter the updataed course")
        ob.ModifyEmployee()
    elif ch == '5':# Display
         pass
    elif ch == '6':
        break


























