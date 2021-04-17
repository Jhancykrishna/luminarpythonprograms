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

    # def __str__(self):
        return self.name

f=(open("marks","r"))

for line in f:
    data=line.split(",")
    # print (data)
    name=data[0]
    rollno=data[1]
    course=data[2]
    mark=int(data[3])
    obj=Student(name,rollno,course,mark)
    obj.printval()
    if(mark>190):
     obj.printval()