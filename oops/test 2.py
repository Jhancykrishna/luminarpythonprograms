class Person:
    def __init__(self,job):
        self.job=job

    def m1(self):
        print("job is",self.job)

class Man(Person):
    def __init__(self,name,age,job):
        super().__init__(job)
        self.name=name
        self.age=age

    def m2(self):
        print("name is",self.name)
        print("age is", self.age)

class Work(Man, Person):
    def __init__(self,company,salary,name,age,job):
        super().__init__(name, age,job)
        self.company = company
        self.salary=salary

    def m3(self):
        print("company name is", self.company)
        print("salary is", self.salary)

emp=Work("luminar",25000,"arun",25,"teacher")
emp.m3()
emp.m2()
emp.m1()
