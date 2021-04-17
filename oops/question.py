# class Person:
#     def setval(self,value):
#         self.value=value
#
#     def printval(self):
#         print( self.value)
#
#
# obj=Person()
# f=(open("C:/Users/USER/PycharmProjects/pythonProject/oops/question","r"))
# for num in f:
#     obj.setval(num)
#     obj.printval()

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printval(self):
        print(self.name)
        print(self.age)

    def __str__(self):
        return self.name

f=(open("C:/Users/USER/PycharmProjects/pythonProject/oops/question","r"))

for line in f:
    data=line.split(",")
    # print (data)
    name=data[0]
    age=data[1]
    obj = Student(name,age)
    # print(obj)
    obj.printval()



