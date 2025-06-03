age = int(input("Enter age: "))
if age < 0:
    raise ValueError("Age cannot be negative!")
print(f"Your age is {age}.")  # This line will not execute if the age is negative
# The code above demonstrates how to raise an exception in Python.