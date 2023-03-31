# Write  a  Python  Program  that  creates  a  class  with  function 
# overloading

class methodOverloading():

    def sum(self, x = 0, y = 0):
        print(x + y)

    def sum(self, x = 0, y = 0, z = 0):
        print(x + y + z)

obj = methodOverloading()

obj.sum(10,20)
obj.sum(10,20,10)
