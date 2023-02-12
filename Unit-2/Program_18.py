# Write a program which accepts a sequence of comma-separated
# numbers from console and generate a list and a tuple which
# contains every number.

num = input("Enter a sequence of comma-separated numbers: ")

numbers_list = num.split(',')
numbers_tuple = tuple(numbers_list)

print("List of numbers: ", numbers_list)
print("Tuple of numbers: ", numbers_tuple)
