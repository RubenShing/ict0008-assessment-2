from datetime import date

from src.book import EBook, HardcopyBook
from src.library import Library


def main():
    library = Library()
    added_on = date(2026, 11, 19)
    author = "J.R.R. Tolkien"
    license_end_date = date(2027, 11, 19)

    library.addBook(HardcopyBook("The Hobbit", author, "9780547928227", True, added_on, "A01"))
    library.addBook(EBook("The Silmarillion", author, "9780618391110", True, added_on, license_end_date))
    library.addBook(HardcopyBook("The Fellowship of the Ring", author, "9780547928210", True, added_on, "A02"))
    library.addBook(EBook("The Two Towers", author, "9780547928203", True, added_on, license_end_date))
    library.addBook(HardcopyBook("The Return of the King", author, "9780547928197", True, added_on, "A03"))

    library.sortBooks()

    print("Community Library Catalogue")
    for book in library.books:
        print(f"{book.isbn} - {book.title} ({book.book_format})")

    while True:
        isbn = input("\nEnter book ISBN (0 = Exit): ").strip()

        if isbn == "0":
            print("Goodbye!")
            break

        book = library.findBookByISBN(isbn)

        if book is None:
            print("Book not found.")
        elif book.borrowBook():
            print("Loan confirmed.")
            book.displayBookDetails()
        else:
            print("Book unavailable.")

if __name__ == "__main__":
    main()