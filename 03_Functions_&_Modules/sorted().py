# sorted()
# Ex :  1 Sorting a List of Numbers
nums = [3, 1, 2]
print(sorted(nums))  # [1, 2, 3]

# Ex :  2 Sorting a List of Strings
strings = ["banana", "apple", "cherry"]
print(sorted(strings))  # ['apple', 'banana', 'cherry']

# Ex :  3 Sorting a List of Tuples by the First Element and then by the Second Element
tuples = [(2, 'b'), (1, 'a'), (3, 'c')]
print(sorted(tuples))  # [(1, 'a'), (2, 'b'), (3, 'c')]
tuples_by_second = sorted(tuples, key=lambda x: x[1])
print(tuples_by_second)  # [(1, 'a'), (2, 'b'), (3, 'c')]

# Ex : 4 Sorting string by length
words = ['apple', 'kiwi', 'banana']
print(sorted(words, key=len))  # ['kiwi', 'apple', 'banana']

# Ex : 5 Sorting with reverse order
print(sorted(nums, reverse=True))  # [3, 2, 1]

