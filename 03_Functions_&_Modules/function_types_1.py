# Based On Definitions

# 1. Built in Functions
# Examples: print(), len(), type(), range(), sorted(), input(), sum()
print(len("Hello"))        # Output: 5
print(sum([1, 2, 3]))      # Output: 6

# 2. User-defined Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))      # Output: Hello, Alice!


# 3. Lambda Functions
square = lambda x: x ** 2
print(square(4))           # Output: 16

# 4. Recursive Functions
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))        # Output: 120

# 5. Higher-order Functions
def double(x):
    return x * 2

def apply(func, value):
    return func(value)

print(apply(double, 10))   # Output: 20

# 6. Generator Functions
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(3):
    print(number)
# Output: 3 2 1


# 7. Decorators
def log(func):
    def wrapper():
        print("Function is about to run")
        func()
        print("Function has finished")
    return wrapper

@log
def say_hello():
    print("Hello!")

say_hello()



