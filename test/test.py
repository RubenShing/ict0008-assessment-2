import unittest
from datetime import date

from src.book import Book


class BookTests(unittest.TestCase):
    def test_book_stores_its_details(self):
        added_on = date(2026, 11, 19)
        book = Book("The Hobbit", "J.R.R. Tolkien", "9780547928227", True, added_on)

        self.assertEqual(book.title, "The Hobbit")
        self.assertEqual(book.author, "J.R.R. Tolkien")
        self.assertEqual(book.isbn, "9780547928227")
        self.assertTrue(book.available)
        self.assertEqual(book.date_added, added_on)

    def test_set_book_details_updates_an_existing_book(self):
        book = Book("Old title", "Old author", "0000000001", True, date(2026, 11, 18))
        added_on = date(2026, 11, 19)

        book.setBookDetails("New title", "New author", "0000000002", False, added_on)

        self.assertEqual(book.title, "New title")
        self.assertEqual(book.author, "New author")
        self.assertEqual(book.isbn, "0000000002")
        self.assertFalse(book.available)
        self.assertEqual(book.date_added, added_on)


if __name__ == "__main__":
    unittest.main()
