# 1.Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. Loop through a string
for char in "hello":
    print(char)

# 3. Loop through a range of numbers
for i in range(5):
    print(i)  # 0 to 4

for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9

# 4. Using else with a for loop
for i in range(3):
    print(i)
else:
    print("Loop completed")

# 5. Using break and continue
for num in range(10):
    if num == 5:
        break
    print(num)

for num in range(5):
    if num == 2:
        continue
    print(num)

# 6. By keys 
person = {"name": "Alice", "age": 30}
for key in person:
    print(key, person[key])

#7. By keys and values
for key, value in person.items():
    print(f"{key} => {value}")

# 8. Nested loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 9. Multiplication table
for i in range(1, 11):
    print(f"Table of {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

# 10. Enumerate and zip
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)
