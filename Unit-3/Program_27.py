# 27 Write a program to read any text file line by line

with open('Sample Text Files/names.txt', 'r') as file:
    for line in file:
        print(line)
