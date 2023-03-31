# Write  a  Python  program  to  overload  __str__  method  of  class 
# and print class values in string format. You can do overloading 
# as  per  your  choice  but  shall  be  done  through  __str__  method 
# only.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
obj = Student('Rohit Luni',20)

print(str(obj))
