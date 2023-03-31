# Write  a  Python  Program  that  creates  a  Student  class  with 
# various methods. Use setattr() and getattr() on class object

class Student():

    def __init__(self,student = 0):
        self.student = student
    def set_student(self, s):
        self.student = s
    def get_student(self):
        return self.student
    

object = Student()

object.set_student(10)

print(object.get_student())