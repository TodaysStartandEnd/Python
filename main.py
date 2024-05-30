## Inheritance
##The parent class passes on methods and data to the child class.
##If a child class wants to use the method of the parent class, it uses super().

class Person :
  def __init__(self, name, age) :
      self.name = name 
      self.age = age
    
  def say_hello(self) :
      print("hello")

  def add_age(self, year) :
      self.age += year

class Timetraveler(Person) :
  def __init__(self, name, age):
   super().__init__(name, age)
    
  def subtract_age(self, year) :
      self.age -= year

class Programmer(Person) :
  def __init__(self, name, age, language) :
    self.name = name 
    self.age = age
    self.language = language

Sunny = Timetraveler("Sunny", 100)
Sunny.subtract_age(10)
print(Sunny.age)

Cloudy = Programmer("Cloudy", 50, "Python")
print(Cloudy.language)





