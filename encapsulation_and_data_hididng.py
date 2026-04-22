# Encapsulation - bundling of data and methods into a class
# the data inside an obect is kept private
# prevents direct access to an object , ensuring integrity and controlled modification
# Data bundling - group related data and methods

# used in - ATMs, Car Dashboard, Medcine Capsule.
# complex internals are hidden behind the simple controlled interface

# python use conventions in naming to enforce
#  when it enconters an attribute with double underscore, it automatically transforms the name through name mangling
# name(public) - can be accessed anywhere
class Animal:
    def __init__(self, name, age):
        self.name = name  # public member
        self.age = age

# _name (protected)- allows subclass use and internal use only
# uses only single underscore


class Animal:
    def __init__(self, name, breed):
        self.name = name  # public member
        self._breed = breed  # protected member

# __name(private) - class can only accessn it
# uses double underscore


class Account:
    def __init__(self, balance):
        self.__balance = balance  # private an on;y be accessed by the class

    def get_balance(self):
        return self.__balance

# Getters and Setters
# they provide controlled acccess to private attributes


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def set_salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            raise ValueError("Salary must be positive")


employee = Employee("Lily Kane", 3000)
print(employee.get_name())
employee.set_salary(4000)
employee.set_salary(333)

# @property
# allows one to access methods at attributes


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            raise ValueError("Invalid Salary")


employee = Employee("Lily Kane", 3000)
print(employee.name)
employee.salary = 4000
print(employee.salary)

# @ property allows us to define methods that can be accessed like attributes, providing a clean and intuitive interface for getting and setting values while still maintaining control over the underlying data.


class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative")


account = BankAccount("123456789", 1000)
print(account.account_number)  # Output: 123456789


@property
def account_info(self):
    return f"Account Number: {self.__account_number}, Balance: {self.__balance}"


def deposit(self, amount):
    if amount > 0:
        self.__balance += amount
    else:
        raise ValueError("Deposit amount must be positive")


account = BankAccount("123456789", 1000)
print(account.balance)  # Output: 1000


def withdraw(self, amount):
    if 0 < amount <= self.__balance:
        self.__balance -= amount
    else:
        raise ValueError("Invalid withdrawal amount")

# Benefits of Encapsulation:
# 1. Data Hiding: Encapsulation allows you to hide the internal state of an object and only expose a controlled interface for interacting with it. This prevents external code from directly accessing and modifying the internal data, ensuring data integrity and security.
# 2. Modularity: Encapsulation promotes modularity by bundling related data and methods together within a class. This makes it easier to manage and maintain code, as changes to the internal implementation of a class do not affect external code that uses the class.
# 3. Code Reusability: Encapsulation allows you to create reusable code by defining classes that can be instantiated multiple times. This promotes code reuse and reduces redundancy, as you can create multiple objects from the same class without having to duplicate code.
# 4. Improved Maintainability: Encapsulation makes it easier to maintain and update code, as changes to the internal implementation of a class do not affect external code that uses the class. This allows for easier debugging and maintenance of code over time.
# 5. Enhanced Security: Encapsulation helps to enhance security by preventing unauthorized access to the internal data of an object. By controlling access through methods, you can implement validation and error handling to ensure that the data is used correctly and securely.
# 6. Integrity: Encapsulation helps to maintain the integrity of an object by controlling how its data is accessed and modified. This ensures that the object remains in a valid state and prevents unintended side effects from external code.
# 7. Reduction of Complexity: Encapsulation helps to reduce complexity by hiding the internal details of an object and providing a simple interface for interacting with it. This allows developers to focus on using the object without needing to understand its internal workings, making it easier to use and understand.
