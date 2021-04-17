class Animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def m1(self):
        print("name:",self.name)
        print("type:",self.type)

class Dog(Animal):
    def __init__(self,color,name,type):
        super().__init__(name,type)
        self.color=color
    def m2(self):
        print("color:",self.color)
ref=Dog("white","MAX","Husky")
ref.m1()
ref.m2()