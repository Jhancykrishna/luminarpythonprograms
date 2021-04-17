#Just to read from file and print maximum mark student complete details
# f=(open("marks","r"))
# list=[]
# for line in f:
#     name,rollno,course,mark=line.rstrip("\n").split(",")
#     # print (name)
#     list.append(mark)
#     if mark==max(list):
#         print(name,rollno,course,mark)
#################################################################
# print(list)
# maxmark=max(list)
# print(maxmark)

    # name=data[0]
    # rollno=data[1]
    # course=data[2]
    # mark=int(data[3])
#####################################################
#OBJECT CREATE AND PRINT MAX STUDENT DETAILS
class Student:
    def __init__(self,name,rollno,course,mark,):
        self.name=name
        self.rollno =rollno
        self.course =course
        self.mark =mark

    def printval(self):
        print(self.name)
        print(self.rollno)
        print(self.course)
        print(self.mark)
    def __str__(self):
        return self.name+self.rollno+ self.course+ self.mark

f=(open("marks","r"))
list=[]
for line in f:
    name, rollno, course, mark = line.rstrip("\n").split(",")
    obj=Student(name,rollno,course,mark)
    # print(obj)
    # obj.printval()
    # list.append(mark)
    # if mark==max(list):
    #     obj.printval()#or print(obj)

    list.append()
    print(list)

#########################################

# bbastud=list(filter(lambda student:))



