# class College:
#     collegename= "LT"
#
#     def __init__(self, name,roll):
#         self.roll=roll
#         self.name=name
#
#     def printdetails(self):
#         print("collegename",self.collegename)
#         print("name of student", self.name)
#         print("rollno", self.roll)
#
#     def __str__(self):
#         return self.name+str(self.roll)
# ob=College("anu",4)
# print(ob)


class Employee:
    companyname = "LT"

    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

    def printval(self):
        print("company:", Employee.companyname)
        print("name:", self.name)
        print("age:", self.age)
        print("id:", self.id)
        print("salary:", self.salary)
    def __str__(self):
        return self.name + str(self.id)


ob = Employee("anu",21,104,20000)
print(ob)