# Write a Python Program to create a function which accepts 3
# arguments. (2 numbers and one arithmetic operator). Display
# answer accordingly

def Calculate(num_1, num_2, operator):
    if operator == '+':
        return num_1 + num_2
    elif operator == '-':
        return num_1 - num_2
    elif operator == '*':
        return num_1 * num_2
    elif operator == '/':
        return num_1 / num_2
    else:
        return print("Enter Valid Operator")


num_1 = int(input("Enter First Number: "))
num_2 = int(input("Enter Second Number: "))

operator = input("Enter Your Operator: ")

result = Calculate(num_1, num_2, operator)

print("Your result is: ", result)
