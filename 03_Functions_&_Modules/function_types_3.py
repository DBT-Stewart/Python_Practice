# Function based on return types

# A. Void Function – Doesn’t return anything
def greet_user(name):
    print(f"[Void] Hello, {name}!")   # Only prints; no return value

result = greet_user("Alice")
print("Return value:", result)        # Output: None


# B. Return Value Function – Returns a single value
def square(number):
    return number ** 2

result = square(5)
print(f"[Return] Square of 5 is: {result}")


# C. Multiple Returns – Returns multiple values as a tuple
def calculate(a, b):
    sum_ = a + b
    diff = a - b
    prod = a * b
    return sum_, diff, prod

s, d, p = calculate(10, 4)
print("[Multiple Returns]")
print(f"  Sum: {s}")
print(f"  Difference: {d}")
print(f"  Product: {p}")
