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

    def returnBook(self):
        self.available = True

    def displayBookDetails(self):
        if self.available:
            status = "Available"
        else:
            status = "Borrowed"

        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Availability: {status}")

    @staticmethod
    def sortBookData(books):
        books.sort(key=lambda book: book.isbn)


class HardcopyBook(Book):
    book_format = "Hardcopy"

    def __init__(self, title, author, isbn, available, date_added, shelf_number):
        super().__init__(title, author, isbn, available, date_added)
        self.shelf_number = shelf_number

    def displayBookDetails(self):
        super().displayBookDetails()
        print(f"Format: {self.book_format}")
        print(f"Shelf number: {self.shelf_number}")


class EBook(Book):
    book_format = "E-book"

    def __init__(self, title, author, isbn, available, date_added, license_end_date):
        super().__init__(title, author, isbn, available, date_added)
        self.license_end_date = license_end_date

    def displayBookDetails(self):
        super().displayBookDetails()
        print(f"Format: {self.book_format}")
        print(f"Licence end date: {self.license_end_date.isoformat()}")
