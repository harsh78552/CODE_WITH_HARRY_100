class Library:
    def __init__(self):
        self.Book = []
        self.book_len = len(self.Book)

    def add_book(self):
        num = int(input("How many books you want to add in library:"))
        for i in range(1, num):
            enter = input("Enter your book: ")
            self.Book.append(enter)
        if num != len(self.Book):
            print("\nBooks not filled properly.")
        else:
            print("OK")

    def no_of_books_entry(self):
        pass

    def Show_Book(self):
        print("\n")
        for index, book in enumerate(self.Book):
            print(f"At index {index} book is {book}")

    def check(self):
        if len(self.Book) == self.book_len:
            print("Ok")
        else:
            print("\nBook are missing.")


E = Library()
E.add_book()
E.no_of_books_entry()
E.Show_Book()
E.check()
