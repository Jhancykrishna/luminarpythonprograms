class Parents:
    def properties(self):
        print("10 lakh rs, 2car")

    def marry(self):
        print("with arun")


class Child(Parents):
    def marry(self):
         print("with ajay")

c=Child()
c.marry()