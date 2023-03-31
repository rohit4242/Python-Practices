# Write a file handling program which shall store Name and 
# BirthDate, it should have 3 choices as follows 
 
# 1)  Add Birth Date 
# 2)  List All Details 
# 3)  Show Today’s Birth Days 
# 4)  Exit 
 
# The  moment  you  start  the  program,  it  shall  first  display  list  of 
# persons who have got birthday today.

import datetime

file_name = "Sample Text Files/birthdays.txt"

def addBirthDate():
    print("========Add Birth Date=========")
    name = input("Enter name: ")
    birthDate = input("Enter birth date (DD/MM/YYYY): ")
    
    with open(file_name, "a") as file:
        file.write(f"{name},{birthDate}\n")
    
    print("Birth date added successfully!")
    
def list_all_details():
    with open(file_name, "r") as file:
        data = file.readlines()
        
        if not data:

            print("No data found!")
        else:
            print("========List All Details=========")
            print("Name\tBirth Date")
            for row in data:
                name,birth_date = row.strip().split(",")

                print(f"{name}\t{birth_date}")
    
def show_todays_birthdays():
    today = datetime.date.today().strftime("%d/%m")
    
    with open(file_name, "r") as file:
        data = file.readlines()
        
        if not data:
            print("No data found!")
        else:
            print("Today's Birthdays")
            for row in data:
                name, birth_date = row.strip().split(",")
                if birth_date.startswith(today):
                    print(name)
    
def exit_program():
    print("Exiting program...")
    exit()

while True:
    show_todays_birthdays()
    
    print("Menu")
    print("1. Add Birth Date")
    print("2. List All Details")
    print("3. Show Today's Birth Days")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        addBirthDate()
    elif choice == "2":
        list_all_details()
    elif choice == "3":
        show_todays_birthdays()
    elif choice == "4":
        exit_program()
    else:
        print("Invalid choice! Please try again.")
