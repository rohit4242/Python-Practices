# Write a program that accepts a comma separated sequence of
# words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program
# :without,hello,bag,world
# Then, the output should be :bag,hello,without,world

words = input("Enter comma separated sequence of words: ")

word = words.split(',')

word.sort()

sorted_word = ','.join(word)

print('Your Sorted Words is: ', sorted_word)
