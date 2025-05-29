# 1 . if statement
age = 18
if age >= 18:
    print("You are an adult.")

# 2. if-else statement
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 3. if-elif-else statement
age = 25
if age < 13:
    print("You are a child.")   
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# 4. Nested if statement
age = 25
if age >= 18:
    print("You are an adult.")
    if age >= 21:
        print("You can drink alcohol in the US.")
        
# 5. One-liner if statement
age = 18
print("You are an adult.") if age >= 18 else print("You are a minor.")