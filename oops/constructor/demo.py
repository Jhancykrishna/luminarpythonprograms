# to intialize value at time of object creation
# class Person:
#     def __init__(self, name,age):
#         self.name=name
#         self.age=age
#
#     def printval(self):
#         print("name:", self.name)
#         print("age:", self.age)
#
#
# obj=Person("anu",23)
# obj.printval()

# class Employee:
#     companyname="luminar"
#     def __init__(self, name,age,id,salary):
#         self.name=name
#         self.age=age
#         self.id = id
#         self.salary = salary
#
#     def printval(self):
#         print("company:",Employee.companyname)
#         print("name:", self.name)
#         print("age:", self.age)
#         print("id:", self.id)
#         print("salary:", self.salary)
#
#
# obj=Employee("ram",23,101,15000)
# obj.printval()
#
# emp1=Employee('arun',26,102,15000)
# obj.printval()

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        sum=self.a+self.b
        print("sub:",sum)

    def sub(self):
        sub=self.a-self.b
        print("sum:",sub)

    def mul(self):
        mul=self.a*self.b
        print("sum:",mul)

    def div(self):
        div=self.a/self.b
        print("div:",div)


obj=Calculator(2,3)
obj.sum()
obj.sub()
obj.mul()
obj.div()