# Class that represents a Library
class Library:

    # Method that accepts different numbers of arguments
    def borrow_book(self, *args):

        # One argument: Book title only
        if len(args) == 1:
            title = args[0]

            print(f"Title: {title}")

        # Two arguments: Book title and borrower
        elif len(args) == 2:
            title = args[0]
            borrower = args[1]

            print(f"Title: {title}")
            print(f"Borrower: {borrower}")

        # Three arguments: Title, borrower, and borrowing duration
        elif len(args) == 3:
            title = args[0]
            borrower = args[1]
            num_days = args[2]

            print(f"Title: {title}")
            print(f"Borrower: {borrower}")
            print(f"Number of Days Borrowed: {num_days}")

        # Invalid number of arguments
        else:
            print("Invalid request! Please try again.")
            return


#object
customer = Library()

print("=" * 50)
print("          LIBRARY BORROWING SYSTEM")
print("=" * 50)

print("\n[ ONE ARGUMENT ]")
print("-" * 50)
customer.borrow_book("Heart Aching")

print("\n[ TWO ARGUMENTS ]")
print("-" * 50)
customer.borrow_book("Wolf Falls in Love with Moon", "Tsukiyama Yuuga")

print("\n[ THREE ARGUMENTS ]")
print("-" * 50)
customer.borrow_book("The Girl I Like Forgot Her Glasses", "Komura", 110)

print()
print("=" * 50)
print("             END OF RECORDS")
print("=" * 50)

print("Edited")

