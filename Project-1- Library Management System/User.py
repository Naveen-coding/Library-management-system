# -*- coding: utf-8 -*-
from Catalog import Catalog
from Book import Book


class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id


class Member(User):
    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issuedbook_list = []

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id

    def searchByName(self, name):
        Catalog.searchByName(name)

    def searchByAuthor(self, author):
        Catalog.searchByAuthor(author)

    def displayAllBooks(self):
        Catalog.displayAllBooks()
    # assume name is unique
    def issueBook(self, name,isbn,days=10):
        self.issuedbook_list.append(isbn)
        Catalog.removeBookItem(isbn)
        print(name,"Book issued for 10 days")

    # assume name is unique
    def returnBook(self, name, isbn, rack):
        for book in self.issuedbook_list:
            if isbn not in self.issuedbook_list:
                print(name,"No book found in the books")
            else:
                self.issuedbook_list.remove(isbn)
                Catalog.addBookItem(name, isbn, rack)
                print(name,"book returned successfully")

class Librarian(User):
    def __init__(self, name, location, age, aadhar_id, emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id

    def __repr__(self):
        return self.name +' '+ self.location +' '+ self.emp_id

    def addBook(self, name, author, publish_date, pages):
        Catalog.addBook(name, author, publish_date, pages)

    def addBookItem(self, name, isbn, rack):
        Catalog.addBookItem(name,isbn, rack)

    def removeBook(self,name):
        Catalog.removeBook(name)

    def removeBookItemFromCatalog(self,isbn):
        Catalog.removeBookItem(isbn)

    def displayAllBooks(self):
        Catalog.displayAllBooks()
