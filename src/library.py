class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def findBookByISBN(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book

        return None