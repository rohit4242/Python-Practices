# Define a class which has at least two methods: 
# getString: to get a string from console input 
# printString: to print the string in upper case. 

class lowerToUpper():

    def getString(self):
        str = input("Enter Your String: ")
        self.string = str

    def printString(self):
        print(self.string.upper())

obj = lowerToUpper()
obj.getString()
obj.printString()