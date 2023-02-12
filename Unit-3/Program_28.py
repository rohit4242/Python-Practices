# Write a program to read text file having number and display all
# numbers with total and average at the last. (Manually prepare a
# file having some numbers and then read it)

with open('Sample Text Files/numbers.txt', 'r') as file:

    count = 0
    total = 0

    for line in file:
        number = float(line)
        print(number)
        total += number

        count += 1


if count > 0:
    average = total / count
else:
    average = 0


print("Your total is:", total)
print("Your average is:", average)
