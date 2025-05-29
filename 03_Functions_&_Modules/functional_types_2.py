#Based on parameters and arguments

# A. Positional Arguments
def introduce_positional(name, age):
    print(f"[Positional] Name: {name}, Age: {age}")

introduce_positional("Alice", 25)  # Positional order matters


# B. Keyword Arguments
def introduce_keyword(name, age):
    print(f"[Keyword] Name: {name}, Age: {age}")

introduce_keyword(age=30, name="Bob")  # Order doesn't matter


# C. Default Arguments
def greet(name="Guest"):
    print(f"[Default] Hello, {name}!")

greet()              # Uses default
greet("Charlie")     # Overrides default


# D. Variable-length Arguments
# 🔹 *args – Tuple of extra positional arguments
def add_all(*args):
    print(f"[Args] Values: {args}, Sum: {sum(args)}")

add_all(1, 2, 3, 4)   # Can pass any number of values

# 🔹 **kwargs – Dictionary of extra keyword arguments
def show_details(**kwargs):
    print("[Kwargs] Details:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

show_details(name="David", age=40, country="USA")


# E. Required (Mandatory) Arguments
def say_hi(name):
    print(f"[Required] Hi, {name}!")

say_hi("Emma")       # ✅ Required argument provided
# say_hi()            # ❌ Uncommenting this will cause an error: missing 1 required argument


# F. Keyword-Only Arguments (Python 3+)
def user_info(name, *, age, country="Unknown"):
    print(f"[Keyword-only] Name: {name}, Age: {age}, Country: {country}")

user_info("Frank", age=29)              # ✅ age must be specified by keyword
user_info("George", age=35, country="UK")
# user_info("Henry", 40)                # ❌ Error: age must be passed as a keyword argument.