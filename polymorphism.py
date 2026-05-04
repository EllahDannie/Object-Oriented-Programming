# Polymorphism - ability of different objects to respond to the same method call in different ways
# Polymorphism is a fundamental concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass.
# It enables a single interface to represent different underlying data types or classes.
# In Python, polymorphism can be achieved through method overriding and duck typing.

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Bird(Animal):
    def speak(self):
        return "Tweet!"
# Function that takes an animal and calls its speak method


def make_animal_speak(animal):
    print(animal.speak())


# Create instances of different animals
dog = Dog()
cat = Cat()
bird = Bird()
# Use the same function to make different animals speak
make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!
make_animal_speak(bird)  # Output: Tweet!
# In this example, we have a base class `Animal` with a method `speak()`.
# The `Dog`, `Cat`, and `Bird` classes inherit from `Animal` and override the `speak()` method to provide their specific implementations.
# The `make_animal_speak` function takes an `Animal` object and calls its
# `speak()` method, demonstrating polymorphism as it can work with any subclass of `Animal` without needing to know the specific type of animal.

# using the same method but displaying different behavior based on the object


class Payment:
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"


class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"


class BankTransferPayment(Payment):
    def process_payment(self, amount):
        return f"Processing bank transfer payment of ${amount}"
# Function to process payment


def process_payment(payment_method, amount):
    print(payment_method.process_payment(amount))


# Create instances of different payment methods
credit_card = CreditCardPayment()
paypal = PayPalPayment()
bank_transfer = BankTransferPayment()
# Process payments using different methods
# Output: Processing credit card payment of $100
process_payment(credit_card, 100)
process_payment(paypal, 150)       # Output: Processing PayPal payment of $150
# Output: Processing bank transfer payment of $200
process_payment(bank_transfer, 200)

# Duck typing - an object is considered to be of a certain type if it has the necessary methods and properties, regardless of its actual class
# done without inheritance or a common base class, as long as the objects have the required methods or properties
# when you use if statements to check for the type of an object, you are not taking advantage of polymorphism and duck typing. Instead, you are relying on explicit type checks, which can lead to less flexible and more error-prone code.


class Book:

    def read(self):
        return "Reading a book"


class Magazine:
    def read(self):
        return "Reading a magazine"


def read_material(material):
    print(material.read())


book = Book()
magazine = Magazine()
read_material(book)
read_material(magazine)

#  inheritancebased polymorphism - relies on a class hierarchy (is-a relationship) where subclasses inherit from a common superclass and override its methods to provide specific implementations.
# duck typing-based polymorphism - relies on behavior (has-a relationship) rather than a class hierarchy. It allows objects of different types to be treated as long as they have the necessary methods or properties, without requiring them to inherit from a common superclass.
