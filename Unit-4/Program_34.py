# Write a Python Program that creates a class and inherit into 
# another class  
# (Base Class : Student with rollno, name, gender, age) 
# (Derived Class : Course with coursename, duration, fee) 
# Use appropriate functions for each class

class Student:
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Age:", self.age)

class Course(Student):
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        super().__init__(rollno, name, gender, age)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee

    def display(self):
        print("===========Student Info===========")
        super().display()
        print("===========Course Info===========")
        print("Course Name:", self.coursename)
        print("Duration:", self.duration)
        print("Fee:", self.fee)

course = Course(1, "Rohit Luni", "Male", 20, "Python", "5 Days", "$0")

course.display()
