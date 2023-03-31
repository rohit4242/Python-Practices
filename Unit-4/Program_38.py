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

    print("6. Exit")
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
        exit(0)







