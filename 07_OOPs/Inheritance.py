# Single Inheritance example in Python
class Animal:
    def speak(self):
        print("Animals make sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create object of Dog
d = Dog()
d.speak()   # Inherited from Animal
d.bark()    # Dog's own method

# Using Super() to call parent class method
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def show(self):
        super().show()
        print(f"Roll No: {self.roll}")

s = Student("Aarav", 101)
s.show()

#Multilevel Inheritance example in Python
class Vehicle:
    def vehicle_info(self):
        print("General Vehicle")

class Car(Vehicle):
    def car_info(self):
        print("This is a Car")

class ElectricCar(Car):
    def electric_info(self):
        print("Runs on electricity")

e = ElectricCar()
e.vehicle_info()
e.car_info()
e.electric_info()

# Multiple Inheritance example in Python
class Father:
    def show_father(self):
        print("Father's traits")

class Mother:
    def show_mother(self):
        print("Mother's traits")

class Child(Father, Mother):
    def show_child(self):
        print("Child inherits from both")

c = Child()
c.show_father()
c.show_mother()
c.show_child()
