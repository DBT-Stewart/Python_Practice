# practice - 1
def greet(name):
    """This function greets the person passed in as a parameter."""
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

#practice - 2
def add_numbers(a, b):
    """This function returns the sum of two numbers."""
    return a + b
print(add_numbers(5, 10))  # Output: 15

#practice - 3
def factorial(n):
    """This function returns the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

#practice - 4
def calculate_area(length, width):
    """This function calculates the area of a rectangle."""
    return length * width
print(calculate_area(5, 10))  # Output: 50

#practice - 5
def calculate_distance(x1, y1, x2, y2):
    """This function calculates the distance between two points."""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(calculate_distance(1, 2, 4, 6))  # Output: 5.0

#practice - 6
def is_prime(num):
    """This function checks if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(7))  # Output: True

#practice - 7
def fibonacci(n):
    """This function returns the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
print(fibonacci(10))  # Output: 55

#practice - 8
print(type(len(input())))