# -*- coding: utf-8 -*-
from Book import Book


# First Book is file & second is Class

class Catalog:
    different_book_count = 0
    books = []

    def addBook(name, author, publish_date, pages):
        b = Book(name, author, publish_date, pages)
        Catalog.different_book_count += 1
        Catalog.books.append(b)
        print("Book added",name)

    def addBookItem(name, isbn, rack):
        for book in Catalog.books:
            if book.name == name:
                b = Book.addBookItem(book,isbn,rack)


    def searchByName(name):
        for book in Catalog.books:
            if book.name == name:
                print("Book Name is available",book.name)
                return book
        else:
            print("Book is not available",name)

    def searchByAuthor(author):
        for book in Catalog.books:
            if book.author == author:
                print("Book Name:"+book.name+"is availble for this author :: "+author)
                break
        else:
            print("Book is not availble for this author :: "+author)

    def displayAllBooks():
        print('Different Book Count', Catalog.different_book_count)
        c = 0
        for book in Catalog.books:
            c += book.total_count
            book.printBook()
        print("Total Books" , c)


    def removeBook(name):
        for book in Catalog.books:
            if book.name == name:
                Catalog.books.remove(book)
                Catalog.different_book_count -= 1
                print("Book removed ",name)

    def removeBookItem(isbn):
        for book in Catalog.books:
            for book_item in book.book_item:
                if book_item.isbn == isbn:
                    book.book_item.remove(book_item)
                    book.total_count -= 1
                    print("Book Item removed successfully from the catalog")
