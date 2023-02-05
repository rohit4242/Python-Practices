# Write a program to create list in such a way that it should add
# square roots of number between 1 to n in the list... At the end,
# the list shall be displayed.
# Example : [1, 4, 9, 16, 25, ....]

def Square_list(n):
    list = []
    for i in range(1, n+1):
        list.append(i**2)
    return list


num = int(input("Enter a number: "))

print("The list of square roots is: ", Square_list(num))
