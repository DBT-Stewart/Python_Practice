# dictionary
# A dictionary is a mutable, unordered collection of key-value pairs in Python.
# Dictionaries are defined using curly braces `{}` or the `dict()` constructor.
# Keys in a dictionary must be unique and immutable, while values can be of any data type.
# Example of creating a dictionary
# Using curly braces
my_dict = {"a": 1, "b": 2}
# Using dict() constructor
other_dict = dict(x=100, y=200)
# Empty dictionary
empty = {}
# Accessing values in a dictionary
print("Value for key 'a':", my_dict["a"])  # Output: 1
# Adding or updating key-value pairs
my_dict["c"] = 3  # Adding a new key-value pair
my_dict["a"] = 10  # Updating an existing key-value pair
print("Updated dictionary:", my_dict)  # Output: {'a': 10, 'b': 2, 'c': 3}
# Removing key-value pairs
# You can remove a key-value pair from a dictionary using the `del` statement or the `pop()` method.
del my_dict["b"]  # Removes the key 'b'
# Using the pop() method to remove a key-value pair
# The pop() method removes the key-value pair with the specified key and returns the value.
# If the key does not exist, it raises a KeyError.
# my_dict.pop("d")  # Raises KeyError: 'd'
print("Dictionary after deletion:", my_dict)  # Output: {'a': 10, 'c': 3}
# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
# Output:
# Key: a, Value: 10
# Key: c, Value: 3  
# Checking if a key exists in a dictionary
print("Is 'a' a key in my_dict?", "a" in my_dict)  # Output: True

contacts = {
    "John": {"phone": "1234", "email": "john@mail.com"},
    "Amy": {"phone": "5678", "email": "amy@mail.com"}
}

# Access Amy’s email
print(contacts["Amy"]["email"])
