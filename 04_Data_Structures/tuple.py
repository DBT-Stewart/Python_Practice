# Tuple

# 1. Definition and Creation
# A tuple is an immutable sequence type in Python, meaning once created, its elements cannot be changed.
# Tuples are defined using parentheses `()`.
# Tuples can contain elements of different data types, including other tuples.
# Example of creating a tuple
coordinates = (10, 20)
# Accessing elements in a tuple
print("X coordinate:", coordinates[0])  # Output: 10
print("Y coordinate:", coordinates[1])  # Output: 20
# Tuples can also be created without parentheses, using commas
coordinates2 = 30, 40
# Accessing elements in a tuple created without parentheses
print("X coordinate 2:", coordinates2[0])  # Output: 30
print("Y coordinate 2:", coordinates2[1])  # Output: 40
# 2. Immutability
# Tuples are immutable, meaning you cannot change their elements after creation.
# Attempting to modify a tuple will raise a TypeError
try:
    coordinates[0] = 15  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)
# 3. Tuple Packing and Unpacking
# Tuples can be packed and unpacked easily.
# Packing a tuple
packed_tuple = (1, 2, 3)
# Unpacking a tuple
a, b, c = packed_tuple
print("Unpacked values:", a, b, c)  # Output: Unpacked values: 1 2 3
# 4. Nested Tuples
# Tuples can contain other tuples, allowing for nested structures.
nested_tuple = (1, (2, 3), (4, 5))
print("Nested tuple:", nested_tuple)  # Output: Nested tuple: (1, (2, 3), (4, 5))
# Accessing elements in a nested tuple
print("First element of nested tuple:", nested_tuple[1][0])  # Output: 2
# 5. Tuple Methods
# Tuples have a limited set of methods compared to lists, as they are immutable.
# Common tuple methods include:
# - `count()`: Returns the number of occurrences of a specified value in the tuple.
# - `index()`: Returns the index of the first occurrence of a specified value in the tuple.
# Example of using tuple methods
example_tuple = (1, 2, 3, 2, 1)
print("Count of 2 in tuple:", example_tuple.count(2))  # Output: 2
print("Index of 3 in tuple:", example_tuple.index(3))  # Output: 2
# 6. Tuple as Dictionary Keys
# Tuples can be used as keys in dictionaries because they are immutable.
# This allows for complex data structures where tuples can represent unique identifiers.
# Example of using a tuple as a dictionary key
point_data = {(10, 20): "Point A", (30, 40): "Point B"}
print("Data for (10, 20):", point_data[(10, 20)])  # Output: Point A
# 7. Tuple Comprehensions
# Tuples can be created using generator expressions, but they are not called comprehensions.
# Example of creating a tuple using a generator expression
squared_numbers = tuple(x ** 2 for x in range(5))
print("Squared numbers tuple:", squared_numbers)  # Output: (0, 1, 4, 9, 16)
# 8. Performance Considerations
# Tuples are generally faster than lists for iteration and access due to their immutability.
# They consume less memory, making them more efficient for fixed collections of items.
# 9. Use Cases
# Tuples are often used to represent fixed collections of items, such as coordinates, RGB colors, or database records.
# They are also used in functions that return multiple values, allowing for easy unpacking.
# Example of a function returning a tuple
def get_coordinates():
    return (10, 20)
x, y = get_coordinates()
print("Returned coordinates:", x, y)  # Output: Returned coordinates: 10 20
# 10. Conclusion
# Tuples are a powerful and efficient data structure in Python, providing immutability and a simple syntax for creating fixed collections of items.
# 11. Tuple Iteration
# Tuples can be iterated over using loops, similar to lists.
for coordinate in coordinates:
    print(coordinate)  # Output: 10, 20
# 12. Tuple Length
# The length of a tuple can be determined using the `len()` function.
print("Length of coordinates tuple:", len(coordinates))  # Output: 2