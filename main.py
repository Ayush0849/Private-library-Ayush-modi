class library:
    def __init__(self,lists_of_books, library_name):
        self.library_name = library_name
        self.lend_record = {}
        self.lists_of_books = lists_of_books
        
        for books in self.lists_of_books:
            self.lend_record[books] = None

    def display_books(self):
        for index, books in enumerate(self.lists_of_books):
            print(f"{index}. {books}")

    def lend_book(self, user, book):
        if book in self.lists_of_books:
            if self.lend_record[book] is None:
                self.lend_record[book] = user
            else:
                print(f'Sorry this book is lend by {self.lend_record[book]}')
        else:
            print("Please enter a valid book name!")
        
    def return_book(self, user, book):
        if book in self.lists_of_books:
            if self.lend_record[book] is not None:
                self.lend_record.pop[book]
            else:
                print('This book is not in the library only or it was never lent')
        else:
            print('Please enter a valid book name!')

    def add_Book(self, user, book):
        self.lists_of_books.append(book)
        self.lend_record[book] = None
    
    def delete_book(self,book_name):
        self.lists_of_books.remove(book_name)
        self.lend_record.pop(book_name)

def main():
    lists_of_books = ['Charlie and the chocolate factory', 'Ghoosebumps', 'The black beauty', 'Sherlock Holmes', 'The women']
    library_name = 'Ayush'
    secret_key = "programming"

    Ayush = library(lists_of_books, library_name)

    print(f"Welcome to {Ayush.library_name}'s library \n 1. Enter 'l' to lend a book\n 2. Enter 'r' to return a book\n 3. Enter 'd' to display the books \n 4. Enter 'a' to add a book \n 5. Enter 'del' to delete a book \n6.Enter 'e' to exit" )
    
    EXit = False
    while (EXit is not True):
        _i = input('Please enter the option: ')
        if _i == 'e':
            print("Thanks for using this program!")
            EXit = True 
        elif _i == 'd':
            Ayush.display_books()
        elif _i == 'l':
            _i1 = input('Please enter your name: ')
            _i2 = input("Enter the name of the book which you want to lend: ")
            print("Book lend")
            Ayush.lend_book(_i1,_i2)
        elif _i == 'r':
            _i3 = input('Please enter your name: ')
            _i4 = input('which book do you want to return: ')
            Ayush.return_book(_i3,_i4)
        elif _i == 'del':
            _i5 = input('Please enter the secret key\n-->')
            if (_i5 == secret_key):
                _i6 = input('Which book do you want to delete: ')
                Ayush.delete_book(_i6)
            else:
                print("Your key is wrong so you cannot delete the book")
        elif _i == 'a':
            _i7 = input('Please enter your name: ')
            _i8 = input('Enter the book name which you want to add: ')
            Ayush.add_Book(_i7,_i8)
            print(f'Thank you {_i7} for donating the book')


if __name__ == "__main__":
    main()


            
    
