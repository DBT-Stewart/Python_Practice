# Ex - 1 : Multiply each number by 10
nums = [1, 2, 3, 4]
result = list(map(lambda x: x * 10, nums))
print(result)  # Output: [10, 20, 30, 40]

# Ex - 2 : Convert each string to uppercase
strings = ["hello", "world", "python"]
result_string = list(map(lambda x: x.capitalize(), strings))
# Output: ['Hello', 'World', 'Python']
result_strings = list(map(lambda x: x.upper(), strings))
# Output: ['HELLO', 'WORLD', 'PYTHON']
print(result_string)
print(result_strings) 