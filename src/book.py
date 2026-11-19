class Book:
    def __init__(self, title, author, isbn, available, date_added):
        self.setBookDetails(title, author, isbn, available, date_added)

    def setBookDetails(self, title, author, isbn, available, date_added):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.date_added = date_added

    def borrowBook(self):
        if not self.available:
            return False

        self.available = False
        return True