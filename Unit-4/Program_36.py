# Write  a  program  that  uses  all  parts  of  exception  handling  in 
# python (try, except, else, finally)

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2

except ValueError:
    print("Invalid input, please enter a valid integer")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("The result is:", result)

finally:
    print("Program execution complete")