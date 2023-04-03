# Create a class of Library with following attributes  
# (title, author, publisher, edition, year of publication, price, type 
# (reference or text book) 
 
# Class shall have following methods 
# addBook(),  modifyBook(),     deleteBook(), searcBook(), 
# listBooks(),   sortedView() 
 
# Prepare menu drive program with the data stored in file. Main 
# menu shall have above choices and sorted view shall have 
# further choice of sorting as title, author, publisher, year of 
# publication and price which shall display the data accordingly) 
# (Use list to store the data as follows 
# [[Core Python Programming|WesleyChun|Premier 
# Press|2|2005|550|Text], 
#   [Pythong Programming for Beginners|Michael|Premier 
# Press|2|2015|660|Reference],  
#   [Head First Python|PaulBerry|O Reilly 
# |4|2014|550|Reference]] 
 
# Data is separated by pipe sign

class Library: 
    def __init__(self):
        self.books = []

    def addBook(self, title, author, publisher, edition, year, price, bookType):
        book = [title, author, publisher, edition, year, price, bookType]
        self.books.append(book)
        writeData(self.books)
    
    def modifyBook(self, title):
        for book in self.books:
            if book[0] == title:
                print(f"Book found: {book}")
                book[1] = input("Enter author name: ")
                book[2] = input("Enter publisher name: ")
                book[3] = input("Enter edition: ")
                book[4] = input("Enter year of publication: ")
                book[5] = input("Enter price: ")
                book[6] = input("Enter book type (reference or text book): ")
                print("Book modified successfully!")
                break
        else:
            print(f"Book not found: {title}")
        
    def deleteBook(self, title):
        for book in self.books:
            if book[0] == title:
                self.books.remove(book)
                print("Book deleted successfully!")
                writeData(self.books)
                break
            else:
                print(f"Book not found: {title}")
    
    def listBooks(self):
        if not self.books:
            print("No books available!")
            return
        print("List of books:")
        for book in self.books:
            print(book)

    
    def searchBook(self, title):
        for book in self.books:
            if book[0] == title:
                print("Book found:")
                print(book)
                break
        else:
            print(f"Book not found: {title}")

    def sortedView(self):
        while True:
            print("1. Sort by Title")
            print("2. Sort by Author")
            print("3. Sort by Publisher")
            print("4. Sort by Year of Publication")
            print("5. Sort by Price")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                sorted_books = sorted(self.books, key=lambda book: book[0])
                print("Sorted by Title:")
                for book in sorted_books:
                    print(book)

            elif choice == '2':
                sorted_books = sorted(self.books, key=lambda book: book[1])
                print("Sorted by Author:")
                for book in sorted_books:
                    print(book)

            elif choice == '3':
                sorted_books = sorted(self.books, key=lambda book: book[2])
                print("Sorted by Publisher:")
                for book in sorted_books:
                    print(book)

            elif choice == '4':
                sorted_books = sorted(self.books, key=lambda book: book[4])
                print("Sorted by Year of Publication:")
                for book in sorted_books:
                    print(book)

            elif choice == '5':
                sorted_books = sorted(self.books, key=lambda book: book[5])
                print("Sorted by Price:")
                for book in sorted_books:
                    print(book)

            elif choice == '6':
                break

            else:
                print("Invalid choice. Please try again.")
         

def readData():
    with open("Sample Text Files/books.txt", "r") as file:
        data = [line.strip().split("|") for line in file]
    return data

def writeData(data):
    with open("Sample Text Files/books.txt", "w") as file:
        for book in data:
            file.write("|".join(book) + "\n")


library = Library()
data = readData()
for book in data:
    library.addBook(*book)

while True:
    print("1. Add Book")
    print("2. Modify Book")
    print("3. Delete Book")
    print("4. List Book")
    print("5. Search Book")
    print("6. Sorted View")

    print("7. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        title = input("Enter title: ")
        author = input("Enter author: ")
        publisher = input("Enter publisher: ")
        edition = input("Enter edition: ")
        year = input("Enter year of publication: ")
        price = input("Enter price: ")
        book_type = input("Enter type (reference or text book): ")
        library.addBook(title, author, publisher, edition, year, price, book_type)
        print("Book added successfully")

    elif choice == '2':
        title = input("Enter title: ")
        library.modifyBook(title)
        
    elif choice == '3':
        title = input("Enter title: ")
        library.deleteBook(title)
      
    elif choice == '4':
        library.listBooks()
    
    elif choice == '5':
        title = input("Enter title: ")
        library.searchBook(title)
 
    elif choice == '6':
        library.sortedView()
    
    elif choice == '7':
        exit(0)







