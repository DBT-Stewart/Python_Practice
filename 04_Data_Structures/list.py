# List :
# Lists are ordered collections of items that can be changed (mutable).
# They can contain elements of different data types and allow duplicate values.
# Lists are defined using square brackets [].

# Example of creating a list
fruits = ["apple", "banana", "cherry"]
# Accessing elements in a list
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry
# Modifying elements in a list
fruits[1] = "orange"
# fruits is now ["apple", "orange", "cherry"]
# Adding elements to a list
fruits.append("kiwi")
# fruits is now ["apple", "orange", "cherry", "kiwi"]
# Inserting elements at a specific position
fruits.insert(1, "mango")
# fruits is now ["apple", "mango", "orange", "cherry", "kiwi"]
# Removing elements from a list
fruits.remove("orange")
# fruits is now ["apple", "mango", "cherry", "kiwi"]
# Popping elements from a list
popped_fruit = fruits.pop(2)  # Removes and returns the element at index 2
# fruits is now ["apple", "mango", "kiwi"]
print(popped_fruit)  # Output: cherry
# Slicing a list
print(fruits[1:3])  # Output: ['mango', 'kiwi']
# List length
print(len(fruits))  # Output: 3
# Checking if an item exists in a list
print("apple" in fruits)  # Output: True
# Iterating through a list
for fruit in fruits:
    print(fruit)
# Output:
# apple
# mango
# kiwi
# List comprehensions
squared_numbers = [x ** 2 for x in range(10)]
# squared_numbers is now [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing elements in a nested list
print(nested_list[0][1])  # Output: 2
# List methods
# append() - adds an element to the end of the list
# extend() - adds elements from another iterable to the end of the list
# sort() - sorts the list in ascending order
# reverse() - reverses the order of elements in the list
# copy() - returns a shallow copy of the list
# Example of using list methods
numbers = [5, 2, 9, 1, 5, 6]
# Sorting a list
numbers.sort()
# numbers is now [1, 2, 5, 5, 6, 9]
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]
# Reversing a list
numbers.reverse()
# numbers is now [9, 6, 5, 5, 2, 1]
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]
# Copying a list
numbers_copy = numbers.copy()
# numbers_copy is now [9, 6, 5, 5, 2, 1]
print(numbers_copy)  # Output: [9, 6, 5, 5, 2, 1]
# List slicing
s = [1, 2, 3, 4, 5]
print(s[1:3])  # Output: [2, 3]
print(s[:3])   # Output: [1, 2, 3]
print(s[3:])   # Output: [4, 5]
# List concatenation
s1 = [1, 2, 3]
s2 = [4, 5, 6]
s3 = s1 + s2
print(s3)  # Output: [1, 2, 3, 4, 5, 6]
# List repetition
s4 = s1 * 2
print(s4)  # Output: [1, 2, 3, 1, 2, 3]
# List membership
print(2 in s1)  # Output: True
print(10 in s1)  # Output: False
# List unpacking
a, b, c = s1
print(a, b, c)  # Output: 1 2 3