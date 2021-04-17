class Employee:
    companyname="luminar"
    def setval(self, name,age,id,salary):
        self.name=name
        self.age=age
        self.id = id
        self.salary = salary

    def printval(self):
        print("company:",Employee.companyname)
        print("name:", self.name)
        print("age:", self.age)
        print("id:", self.id)
        print("salary:", self.salary)


obj=Employee()
obj.setval("ram",23,101,15000)
obj.printval()

emp1=Employee()
emp1.setval('arun',26,102,15000)
obj.printval()