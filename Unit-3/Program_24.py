# Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence
# capitalized. If you enter blank line, shall be treated as exit of
# program. All the upper case converted lines shall be added to
# list one by one 

lines = []
while True:
    line = input("Enter a line (press Enter to exit): ")
    if line == '':
        break
    else:
        capitalized_line = line.upper()
        lines.append(capitalized_line)

print("Capitalized lines:")
for line in lines:
    print(line)
