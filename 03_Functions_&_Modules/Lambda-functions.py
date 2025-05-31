# Lambda functions are small anonymous functions defined with the `lambda` keyword.
# They can take any number of arguments but can only have one expression.
# Lambda functions are often used for short, throwaway functions that are not reused elsewhere.


# Ex : 1 Sorting Tuples based on second Element
pairs = [(1, 3), (2, 1), (5, 2),(0, 0)]
sorted_pairs = sorted(pairs)
# This sorts the list of tuples based on the first element of each tuple
sorted_pairs_2 = sorted(pairs, key=lambda x: x[1])
# This sorts the list of tuples based on the second element of each tuple
print(sorted_pairs)  # Output: [(0, 0), (1, 3), (2, 1), (5, 2)]
print(sorted_pairs_2) # Output: [(0, 0), (2, 1), (5, 2), (1, 3)]

# Ex : 2 Filtering Numbers from a List using filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# This filters the list to include only even numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# This filters the list to include only odd numbers
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Ex : 3 Squaring Values in a List using map()
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
cube = list(map(lambda x: x ** 3, nums))
print(squared)  # Output: [1, 4, 9, 16]
print(cube)  # Output: [1, 8, 27, 64]

