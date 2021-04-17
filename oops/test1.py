class Vehicle:
    def __init__(self,name,price):
        self.name=name
        self.price=price


    def printval(self):
        print("name",self.name)
        print("price",self.price)


class Bus(Vehicle):
    def __init__(self, company,name,price):
       super().__init__(name,price)
       self.company =company


    def print(self):
        print("company name",self.company)

cr=Bus("XYZ","KSRTC",200000)
cr.printval()
cr.print()

