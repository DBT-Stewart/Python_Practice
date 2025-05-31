# 1. Break Statement
for i in range(10):
    if i == 5:
        print("Breaking at i =", i)
        break  # Exits the loop when i is 5
    print("i =", i)

# 2. Continue Statement
for i in range(10):
    if i % 2 == 0:
        print("Skipping even number:", i)
        continue  # Skips the rest of the loop for even numbers
    print("Odd number:", i)

# 3. Pass Statement
for i in range(5):
    if i == 2:
        print("Pass at i =", i)
        pass  # Does nothing, just a placeholder
    print("i =", i)

# 4. else Statement with Loops
for i in range(3):
    print("Looping:", i)
else:
    print("Loop completed without break.")

for i in range(3):
    print("Looping:", i)
    if i == 2:
        print("Breaking at i =", i)
        break  # This will exit the loop before reaching else
else:
    print("Loop completed without break.")

# 5. match Statement (Python 3.10+)
day = input("Enter a day of the week: ")

match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Almost weekend!")
    case _:
        print("Other day")
