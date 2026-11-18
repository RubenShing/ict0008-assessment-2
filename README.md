# ICT0008 Assessment 2

A Python console program for a community library. It will load five books, sort them by ISBN, and let the user borrow a book by entering its ISBN. Enter 0 to exit.

## Testing plan

- Check that five books load in ISBN order.
- Borrow an available book and check that it becomes unavailable.
- Try to borrow the same book again and check that the request is rejected.
- Return a borrowed book and check that it becomes available again.
- Enter an unknown ISBN and check that the prompt repeats after a message.
- Enter 0 and check that the program exits.

Automated tests will be added to `test/test.py`. These checks are planned.
