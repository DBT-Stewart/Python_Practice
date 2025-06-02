# Sets

# Example of using sets in Python
# Sets are unordered collections of unique elements.
# They are defined using curly braces {} or the set() constructor.

# Example of creating a set
fruits = {"apple", "banana", "cherry"}
# Accessing elements in a set
# Note: Sets do not support indexing, so you cannot access elements by index.
print(fruits)  # Output: {'apple', 'banana', 'cherry'}
# Adding elements to a set
fruits.add("kiwi")
# fruits is now {'apple', 'banana', 'cherry', 'kiwi'}
# Removing elements from a set
fruits.remove("banana")
# fruits is now {'apple', 'cherry', 'kiwi'}
# Popping an element from a set
try:
    fruits.pop()
except KeyError:
    print("Set is empty")

# fruits is now {'cherry', 'kiwi'} (the popped element is arbitrary)
# Checking if an element is in a set
print("apple" in fruits)  # Output: True
# Iterating through a set
for fruit in fruits:
    print(fruit)
# Output:
# cherry       
# kiwi
# Checking if a set is a subset of another set
set1 = {"apple", "banana"}
set2 = {"apple", "banana", "cherry"}
print(set1.issubset(set2))  # Output: True
# Checking if a set is a superset of another set
print(set2.issuperset(set1))  # Output: True
# Set operations
# Union of two sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_union = set_a.union(set_b)
print(set_union)  # Output: {1, 2, 3, 4, 5}
# Intersection of two sets
set_intersection = set_a.intersection(set_b)
print(set_intersection)  # Output: {3}
# Difference between two sets
set_difference = set_a.difference(set_b)
print(set_difference)  # Output: {1, 2}
# Symmetric difference between two sets
set_symmetric_difference = set_a.symmetric_difference(set_b)
print(set_symmetric_difference)  # Output: {1, 2, 4, 5}
# Set comprehensions
squared_numbers = {x ** 2 for x in range(5)}
print(squared_numbers)  # Output: {0, 1, 4, 9, 16}
# Nested sets
nested_set = {1, 2, {3, 4}}
print(nested_set)  # Output: {1, 2, {3, 4}}
# Performance considerations
# Sets are generally faster than lists for membership tests (checking if an element exists).
# They are implemented using hash tables, which allows for average O(1) time complexity for lookups.
# Use cases
# Sets are useful when you need to store a collection of unique elements, such as:
# - Removing duplicates from a list
# - Performing mathematical set operations (union, intersection, etc.)
# - Checking for membership in a collection
# Example of using sets in Python
def main():
    # Creating a set
    fruits = {"apple", "banana", "cherry"}
    print("Initial set:", fruits)

    # Adding an element
    fruits.add("kiwi")
    print("After adding kiwi:", fruits)

    # Removing an element
    fruits.remove("banana")
    print("After removing banana:", fruits)

    # Popping an element
    popped_fruit = fruits.pop()
    print("Popped fruit:", popped_fruit)
    print("Set after popping an element:", fruits)

    # Checking membership
    print("Is 'apple' in the set?", "apple" in fruits)

    # Iterating through the set
    print("Iterating through the set:")
    for fruit in fruits:
        print(fruit)
    
    