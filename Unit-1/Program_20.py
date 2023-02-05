# Write a Python Program to create function which accepts one
# argument as a number and return Factorial value of the
# number. (Function must be RECURSIVE function, not loop)

def factorial(n):
    if n == 0:
        return 1

    else:
        return n * factorial(n-1)


num = int(input("Enter a number: "))

print(f'The factorial {num} is: {factorial(num)}')
