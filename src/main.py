from datetime import date

from src.book import Book
from src.library import Library


def main():
    library = Library()
    added_on = date(2026, 11, 19)
    author = "J.R.R. Tolkien"

    library.addBook(Book("The Hobbit", author, "9780547928227", True, added_on))
    library.addBook(Book("The Silmarillion", author, "9780618391110", True, added_on))
    library.addBook(Book("The Fellowship of the Ring", author, "9780547928210", True, added_on))
    library.addBook(Book("The Two Towers", author, "9780547928203", True, added_on))
    library.addBook(Book("The Return of the King", author, "9780547928197", True, added_on))

    library.sortBooks()

    print("Community Library Catalogue")
    for book in library.books:
        print(f"{book.isbn} - {book.title}")


if __name__ == "__main__":
    main()