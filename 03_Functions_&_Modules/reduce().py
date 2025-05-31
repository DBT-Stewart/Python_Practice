# reduce()
from functools import reduce

# Ex : 1 Calculate the product of all elements in a list
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print("Product of all elements:", product)  # Output: 24

# Ex : 2 Find the maximum value in a list
numbers = [5, 2, 9, 1, 5, 6]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum value:", max_value)  # Output: 9

# Ex : 3 Concatenate a list of strings
words = ['Hello', 'World', 'Python']
sentence = reduce(lambda x, y: x + ' ' + y, words)
print(sentence)  # "Hello World Python"

