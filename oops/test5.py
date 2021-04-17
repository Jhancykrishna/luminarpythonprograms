class Book:
    def library(self, libraryname):
        self.libraryname = libraryname
        print("library_name:", self.libraryname)
    def m1(self,bookname):
        self.bookname = bookname
        print("book_name:", self.bookname)
class Kidsbook(Book):
    def m1(self, author,pages):
        self.author = author
        self.pages = pages
        print("author:", self.author)
        print("pages:", self.pages)

obj=Kidsbook()
obj.library("xyz")
obj.m1("r bond",200)
