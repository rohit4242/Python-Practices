# Write a program to read names from keyboard and store into
# text file

with open('Sample Text Files/names.txt', 'w') as file:
    while True:
        names = input("Enter a name (press Enter to exit): ")
        if names == '':
            break
        file.write(names+'\n')

print("Your name is store into names.txt file")
