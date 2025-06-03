# Types of exceptions in python
import requests

# 1. ZeroDivisionError
def zero_division_error():
    try:
        print(10 / 0)
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")

# 2. ValueError
def value_error():
    try:
        num = int(input("Enter a number: "))
        print(10 / num)
    except ValueError as e:
        print(f"ValueError: {e}")

# 3. FileNotFoundError
def file_not_found_error():
    try:
        with open("non_existent_file.txt", "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")

# 4. IndexError
def index_error():
    try:
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError as e:
        print(f"IndexError: {e}")

# 5. KeyError
def key_error():
    try:
        my_dict = {"a": 1, "b": 2}
        print(my_dict["c"])
    except KeyError as e:
        print(f"KeyError: {e}")

# 6. TypeError
def type_error():
    try:
        result = "string" + 5
    except TypeError as e:
        print(f"TypeError: {e}")

# 7. AttributeError
def attribute_error():
    try:
        my_list = [1, 2, 3]
        my_list.append(4)
        my_list.non_existent_method()
    except AttributeError as e:
        print(f"AttributeError: {e}")

# 8. ImportError
def import_error():
    try:
        raise ImportError("No module named 'non_existent_module'")
    except ImportError as e:
        print(f"ImportError: {e}")

# 9. NameError
def name_error():
    try:
        raise NameError("undefined_variable is not defined")
    except NameError as e:
        print(f"NameError: {e}")

# 10. OSError
def os_error():
    try:
        import os
        os.remove("non_existent_file.txt")
    except OSError as e:
        print(f"OSError: {e}")

# 11. RuntimeError
def runtime_error():
    try:
        raise RuntimeError("This is a runtime error.")
    except RuntimeError as e:
        print(f"RuntimeError: {e}")

# 12. StopIteration
def stop_iteration():
    try:
        my_iter = iter([1, 2, 3])
        while True:
            print(next(my_iter))
    except StopIteration as e:
        print(f"StopIteration: {e}")

# 13. MemoryError
def memory_error():
    try:
        large_list = [1] * (10**10)  # Attempt to allocate a large list
    except MemoryError as e:
        print(f"MemoryError: {e}")

# 14. RecursionError
def recursion_error():
    try:
        def recursive_function():
            return recursive_function()
        recursive_function()
    except RecursionError as e:
        print(f"RecursionError: {e}")

# 15. AssertionError
def assertion_error():
    try:
        assert False, "This is an assertion error."
    except AssertionError as e:
        print(f"AssertionError: {e}")

# 16. NotImplementedError
def not_implemented_error():
    try:
        raise NotImplementedError("This feature is not implemented yet.")
    except NotImplementedError as e:
        print(f"NotImplementedError: {e}")

# 17. UnicodeError
def unicode_error():
    try:
        invalid_unicode = b'\x80'  # Invalid byte sequence
        invalid_unicode.decode('utf-8')
    except UnicodeError as e:
        print(f"UnicodeError: {e}")

# 18. TimeoutError
def timeout_error():
    try:
        import time
        time.sleep(5)  # Simulating a long operation
        raise TimeoutError("The operation timed out.")
    except TimeoutError as e:
        print(f"TimeoutError: {e}")

# 19. ConnectionError
def connection_error():
    try:
        import requests
        response = requests.get("http://non_existent_url.com")
        response.raise_for_status()
    except requests.ConnectionError as e:
        print(f"ConnectionError: {e}")

# 20. HTTPError
def http_error():
    try:
        import requests
        response = requests.get("http://httpbin.org/status/404")
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f"HTTPError: {e}")
