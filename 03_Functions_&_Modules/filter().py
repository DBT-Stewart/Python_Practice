# filter()
# The `filter()` function is used to filter elements from an iterable (like a list) based on a function that returns True or False.

# Ex - 1 : Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# This filters the list to include only even numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# This filters the list to include only odd numbers
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Ex - 2 : Filter strings that start with a specific letter
strings = ["apple", "banana", "cherry", "date", "berry"]
filtered_strings = list(filter(lambda x: x.startswith('b'), strings))
# This filters the list to include only strings that start with 'b'
print(filtered_strings)  # Output: ['banana', 'berry']

# Ex - 3 : Filter numbers greater than a certain value
numbers = [10, 20, 30, 40, 50]
greater_than_25 = list(filter(lambda x: x > 25, numbers))
# This filters the list to include only numbers greater than 25
print(greater_than_25)  # Output: [30, 40, 50]