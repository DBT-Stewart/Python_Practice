# 1. Map
# This function applies a given function to all items in an iterable (like a list) and returns a map object.
# general usage:
numbers = [1, 2, 3, 4, 5]

def square(n):
    return n * n

squared_numbers = map(square, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# by maping
numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * x, numbers)))

# 2. Filter
# This function filters items out of an iterable based on a function that returns True or False.
# general usage:
numbers = [1, 2, 3, 4, 5, 6]

def is_even(n):
    return n % 2 == 0

even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # Output: [2, 4, 6]

# by filtering
numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, numbers)))

# 3. Reduce
# This function applies a rolling computation to sequential pairs of values in an iterable.
# general usage:
from functools import reduce

numbers = [1, 2, 3, 4, 5]

def multiply(x, y):
    return x * y

product = reduce(multiply, numbers)

print(product)  # Output: 120

# by reducing
numbers = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x * y, numbers))  # Product: 120