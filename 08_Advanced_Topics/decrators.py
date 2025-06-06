# ex 1
def decorator_func(original_func):
    def wrapper():
        print("Before function call")
        original_func()
        print("After function call")
    return wrapper

@decorator_func
def say_hello():
    print("Hello!")

say_hello()

# ex 2
# This is our decorator
def my_decorator(func):
    def wrapper():
        print("Hello from decorator! 👋")
        func()
        print("Goodbye from decorator! 👋")
    return wrapper

# Using the decorator
@my_decorator
def greet():
    print("I'm the original function!")

# Calling the function
greet()
