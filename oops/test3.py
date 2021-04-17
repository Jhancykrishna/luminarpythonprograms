class Book:

    def m1(self,libraryname):
          self.libraryname=libraryname
          print("library_name:",self.libraryname)

    def m2(self,bookname):
          self.bookname=bookname
          print("book_name:",self. bookname)

    def m3(self,author):
          self.author=author
          print("author:",self.author)

    def m4(self,pages):
          self.pages = pages
          print("pages:",self.pages)
obj=Book()
obj.m1("xyz")
obj.m2("cherry tree")
obj.m3("ruskin bond")
obj.m4("200")

#
# class Book:
#     def __init__(self,libraryname,bookname,author,pages):
#         self.libraryname=libraryname
#         self.bookname=bookname
#         self.author=author
#         self.pages=pages
#
#     def print(self):
#         print("libraryname =",self.libraryname)
#         print("bookname =",self.bookname)
#         print("author =",self.author)
#         print("pages =",self.pages)
#
# obj=Book("xyz","cherry tree","ruskin bond",200)
# obj.print()