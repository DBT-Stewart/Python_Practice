# Basic Encapsulation Example
class Student:
    def __init__(self, name, age):
        self.__name = name     # private variable
        self.__age = age       # private variable

    def show(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age

s = Student("Arya", 20)
s.show()
s.set_age(21)
print("Updated age:", s.get_age())

# Direct access will fail:
# print(s.__age)  # ❌ Error

# Protected Varaiables Example
class Person:
    def __init__(self):
        self._address = "Hidden Street"

class Employee(Person):
    def show_address(self):
        print(f"Address: {self._address}")

e = Employee()
e.show_address()

# Bank Account With Encapsulation Example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print("Balance:", acc.get_balance())
