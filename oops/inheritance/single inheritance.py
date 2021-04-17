# class Parent:
#     parent_name="arun"
#     def m1(self,age):
#         self.age=age
#         print("my name is",Parent.parent_name)
#         print(self.age)
#
# class Child(Parent):
#     def m2(self,cage):
#         self.cage=cage
#         print("parent name is",Parent.parent_name)
#         print(self.age)
#         print(self.cage)
#
# c=Child()
# c.m1(23)
# c.m2(10)

class Parent:
    parent_name="arun"
    def m1(self,age):
        self.age=age
        print("my name is",Parent.parent_name)
        print(self.age)

class Child(Parent):
    child_name="raj"
    def m2(self):
        print("my name is",Child.child_name)

c=Child()
c.m1(23)
c.m2()
