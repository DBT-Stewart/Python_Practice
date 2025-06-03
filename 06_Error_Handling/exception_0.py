# Exception Handling in Python
#print(10 / 0)  # ❌ ZeroDivisionError

# Exception Handling in Python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Great! No errors occurred.")
finally:
    print("Execution finished.")