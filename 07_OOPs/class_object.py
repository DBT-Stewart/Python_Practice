class goa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the class
obj = goa("Alice", 30)
# Accessing the object's attributes and methods
obj.display()
# Output: Name: Alice, Age: 30
# Creating another object of the class
obj2 = goa("Bob", 25)
# Accessing the second object's attributes and methods
obj2.display()
# Output: Name: Bob, Age: 25