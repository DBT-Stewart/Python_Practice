# 1. Numeric Types (int, float, complex)
a = 10
print("Integer:", a, type(a))

b = 3.14
print("Float:", b, type(b))

c = 2 + 3j
print("Complex:", c, type(c))

# 2. String Type
name = "Python"
print("String:", name, type(name))

print("Uppercase:", name.upper())
print("First letter:", name[0])
print("Slicing:", name[1:4])

# 3. Boolean Type
is_active = True
print("Boolean:", is_active, type(is_active))

print("True and False:", True and False)
print("True or False:", True or False)

# 4. List Type
is_active = True
print("Boolean:", is_active, type(is_active))

print("True and False:", True and False)
print("True or False:", True or False)

# 5. Tuple Type
coordinates = (10, 20)
print("Tuple:", coordinates, type(coordinates))

print("X coordinate:", coordinates[0])

# 6. Set Type
unique_numbers = {1, 2, 3, 2, 1}
print("Set (no duplicates):", unique_numbers, type(unique_numbers))

unique_numbers.add(4)
print("After adding 4:", unique_numbers)

# 7. Dictionary Type
student = {"name": "Alice", "age": 22}
print("Dictionary:", student, type(student))

print("Name:", student["name"])
student["grade"] = "A"
print("Updated Dictionary:", student)

# 8. Type Conversion
x = "100"
y = int(x)
print("Converted to int:", y, type(y))

z = float(y)
print("Converted to float:", z, type(z))