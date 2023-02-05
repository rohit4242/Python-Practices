# Write a program to input a number and display Table of that
# number.

num = int(input("Enter Your Number: "))

for i in range(1, 11):
    print(f'{num} X {i} = {num * i}')
