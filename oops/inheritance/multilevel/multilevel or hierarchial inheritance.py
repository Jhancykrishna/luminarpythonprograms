class Addition:

    def m1(self, a, b):
        self.a = a
        self.b = b
        sum = self.a + self.b
        print("suM:", sum)
class Subtraction(Addition):

    def m2(self):
        sub = self.a - self.b
        print("suB:", sub)


class Calc(Subtraction):

    def m3(self):
        mul = self.a * self.b
        print("MUL:", mul)

    def m4(self):
        div = self.a / self.b
        print("DIV:", div)

c=Calc()
c.m1(2,3)
c.m2()
c.m3()
c.m4()
c=Subtraction()
c.m1(2,3)
c.m2()