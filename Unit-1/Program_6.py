# Write a program to input age of person and display message as
# follows
# - If age < 12 print You are Kid
# - If age between 12 to 17 print You are teenager
# - If age between 18 to 60 print you are Adult
# If age > 60 print You are Senior Citizen

Age = int(input("Enter Your Age: "))

if Age >= 1 and Age <= 100:
    if Age <= 12:
        print("You Are Kid")
    elif Age >= 12 and Age <= 17:
        print("You are teenager")
    elif Age >= 18 and Age <= 60:
        print("You are Adult")
    elif Age >= 60:
        print("You are Senior Citizen")
else:
    print("Enter Valide Age")
