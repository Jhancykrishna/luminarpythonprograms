class Employee:

    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def print(self):
        print(self.ename)

f=open("employees")
employees=[]
for lines in f:
    # data=lines.rstrip("\n").split(",")
    eid,name,desig,sal=lines.rstrip("\n").split(",")
    e1=Employee(eid,name,desig,sa)


for emp in employees:
    print(emp.design)
salaries=list(map(lambda emp:emp.salary,employees))


developers=list(filter(lambda emp:emp.design))