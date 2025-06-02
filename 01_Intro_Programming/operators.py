# 1 . Arti=hmetic Operators
a = 15
b = 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

#2. Assignment Operators
x = 10
x += 5
print("After += :", x)
x *= 2
print("After *= :", x)
x -= 3
print("After -= :", x)
x /= 4
print("After /= :", x)

# 3. Comparison Operators
a = 10
b = 20
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)

# 4. Logical Operators
x = True
y = False

print("AND:", x and y)
print("NOT x:", not x)

# 5. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)
print("a is c:", a is c)
print("a == c:", a == c)

# 6. Membership Operators
fruits = ["apple", "banana", "cherry"]

print("Is 'apple' in list?", "apple" in fruits)
print("Is 'grape' not in list?", "grape" not in fruits)

# 7. Bitwise Operators
a = 5  # 0101
b = 3  # 0011

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT a:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

# 8. Ternary Operator
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)