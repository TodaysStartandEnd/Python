## Class 
## method + variable
## 1. method(functions in class) : The first parameter of the method points to the address of the object itself.

class Person :
  def __init__(self) :
      print (self) ##<__main__.Person object at 0x7901da58ebf0>
      self.name = "Sunny"
      self.age = 100
      

Doctor = Person()
print(Doctor) ## <__main__.Person object at 0x7901da58ebf0>
print(Doctor.name); ##Sunny
print(Doctor.age);##100



