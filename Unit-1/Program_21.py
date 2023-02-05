# Write a program to create lambda function to add two numbers
# and display total.

def add(num_1, num_2): return num_1+num_2


num_1 = int(input("Enter First Number: "))
num_2 = int(input("Enter Second Number: "))

print(f'Sum of The numbers is: {add(num_1,num_2)}')
