# -*- coding: utf-8 -*-

from User import Member
from User import Librarian

lib = Librarian("Naveen", "AP", 22, "AA123", "EMP123")
print(lib)

lib.addBook('Shoe Dog','Phil Knight', "2015",400)
lib.addBookItem("Shoe Dog", "isbn1", "H1B1")
lib.addBookItem("Shoe Dog", "isbn3", "H1B2")
lib.displayAllBooks()
lib.addBook('Progrmming','imran khan', "1999",500)
lib.addBookItem("Progrmming", "isbn4", "H1C1")
lib.addBookItem("Progrmming", "isbn6", "H1C2")
lib.displayAllBooks()
lib.addBook('Python','reema thareja', "200",320)
lib.addBookItem("Python", "isbn7", "H1D1")
lib.addBookItem("Python", "isbn9", "H1D2")
lib.displayAllBooks()


lib.removeBook("Python")
lib.displayAllBooks()

lib.removeBookItemFromCatalog("isbn1")
lib.displayAllBooks()


m1 = Member("Sharma", "Ap", 20, "AA990", "STUID112")
print(m1)

m1.searchByName("Shoe Dog")

m1.searchByAuthor('imran khan')

m1.displayAllBooks()

m1.issueBook("Progrmming", "isbn4")

m1.displayAllBooks()

m1.returnBook("Progrmming", "isbn4","H1C1")

m1.displayAllBooks()
