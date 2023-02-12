# Write a program to compute the frequency of the words from
# the input. The output should output after sorting the key
# alphanumerically.
# Suppose the following input is supplied to the program:
# “Hello There this is Python. Python is good”
# Then output shall be as follows :
# Hello : 1
# There : 1
# This : 1
# is : 2
# Python : 2
# Good : 1

input_string = input("Enter Your words:")

words = input_string.split()

print(words)
frequency = {}

for word in words:

    frequency[word] = frequency.get(word, 0) + 1


print("=============Without Sorted key=============")
for key, value in frequency.items():
    print(f'{key.capitalize()} : {value}')


print("=============With Sorted Key=============")
sorted_key = sorted(frequency.keys())

for key in sorted_key:
    print(f'{key.capitalize()} : {frequency[key]}')
