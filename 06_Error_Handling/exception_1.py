try:
    file = open("data.txt")
except FileNotFoundError:
    print("File missing!")
else:
    print("File opened successfully.")
finally:
    print("Cleaning up.")
# The code above demonstrates exception handling in Python.

try:
    print(10 / 0)
except:
    print("Oops! Something went wrong.")
else:
    print("No errors occurred.")